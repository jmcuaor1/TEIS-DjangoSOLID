import os
import sys
from .gateways import BancoNacionalProcesador


class MockPaymentProcessor:
    def pagar(self, monto: float) -> bool:
        mensaje = f"[DEBUG] Mock Payment: Procesando pago de ${monto} sin cargo real."
        print(mensaje, flush=True)
        sys.stdout.flush()
        # También lo guardamos en un archivo para tener evidencia
        with open("mock_payment.log", "a") as f:
            f.write(mensaje + "\n")
        return True


class PaymentFactory:
    @staticmethod
    def get_processor():
        provider = os.getenv('PAYMENT_PROVIDER', 'BANCO')

        if provider == 'MOCK':
            return MockPaymentProcessor()

        return BancoNacionalProcesador()