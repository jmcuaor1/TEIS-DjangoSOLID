import datetime
from ..domain.interfaces import ProcesadorPago

class BancoNacionalProcesador(ProcesadorPago):

    def pagar(self, monto: float) -> bool:
        archivo_log = "pagos_locales_JUAN_MIGUEL_CUAO.log"
        
        with open(archivo_log, "a") as f:
            f.write(f"[{datetime.datetime.now()}] BANCO NACIONAL - Cobro procesado: ${monto}\n")
        return True