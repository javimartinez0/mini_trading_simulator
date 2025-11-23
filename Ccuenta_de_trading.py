from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict

@dataclass
class CuentaDeTrading:
    saldo: float = 0.0
    historial_operaciones: List[Dict] = field(default_factory=list)

    def depositar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo.")
        self.saldo += monto

    def retirar(self, monto: float) -> None:
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo.")
        if monto > self.saldo:
            raise ValueError("Fondos insuficientes.")
        self.saldo -= monto

    def registrar_operacion(
        self,
        fecha: datetime,
        instrumento: str,
        tipo: str,  # ej. "compra" / "venta"
        tamano: float,
        precio_entrada: float,
        precio_salida: float,
        resultado: float,
        fecha_cierre: datetime | None = None,
    ) -> None:
        operacion = {
            "fecha": fecha,
            "instrumento": instrumento,
            "tipo": tipo,
            "tamano": tamano,
            "precio_entrada": precio_entrada,
            "precio_salida": precio_salida,
            "resultado": resultado,
        }
        if fecha_cierre is not None:
            operacion["fecha_cierre"] = fecha_cierre
        self.historial_operaciones.append(operacion)
        self.saldo += resultado  # asumiendo que resultado ya incluye P&L neto
