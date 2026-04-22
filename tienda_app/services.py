from django.shortcuts import get_object_or_404
import sys

from .domain.builders import OrdenBuilder
from .domain.logic import CalculadorImpuestos
from .models import Inventario, Libro


class CompraService:

    def __init__(self, procesador_pago):
        self.procesador_pago = procesador_pago
        self.builder = OrdenBuilder()

    def obtener_detalle_producto(self, libro_id):
        libro = get_object_or_404(Libro, id=libro_id)
        total = CalculadorImpuestos.obtener_total_con_iva(libro.precio)
        return {"libro": libro, "total": total}

    def ejecutar_compra(self, libro_id, cantidad=1, direccion="", usuario=None):
        print(">>> PASO 1: Buscando libro...", flush=True)
        libro = get_object_or_404(Libro, id=libro_id)
        
        print(">>> PASO 2: Buscando inventario...", flush=True)
        inv = get_object_or_404(Inventario, libro=libro)

        print(f">>> PASO 3: Stock disponible: {inv.cantidad}", flush=True)
        if inv.cantidad < cantidad:
            raise ValueError("No hay suficiente stock para completar la compra.")

        print(">>> PASO 4: Construyendo orden...", flush=True)
        orden = (
            self.builder
            .con_usuario(usuario)
            .con_libro(libro)
            .con_cantidad(cantidad)
            .para_envio(direccion)
            .build()
        )

        print(">>> PASO 5: Procesando pago...", flush=True)
        pago_exitoso = self.procesador_pago.pagar(orden.total)
        if not pago_exitoso:
            orden.delete()
            raise Exception("La transacción fue rechazada por el banco.")

        inv.cantidad -= cantidad
        inv.save()

        print(">>> PASO 6: Compra completada!", flush=True)
        return orden.total
    