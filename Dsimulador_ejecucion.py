import Acargar_y_limpiar_csv
import Bgenerar_senales
from Ccuenta_de_trading import CuentaDeTrading


def ejecutar_trading(ruta_csv: str, saldo_inicial: float = 0.0) -> CuentaDeTrading:
    """
    Backtest: limpia el CSV, genera senales y mantiene la posicion abierta
    hasta recibir la senal contraria. Usa un tamano de operacion fijo de 1.0.
    Cierra cualquier posicion pendiente al final con el ultimo precio disponible.
    saldo_inicial define el balance de partida de la cuenta.
    """
    if saldo_inicial < 0:
        raise ValueError("El saldo inicial no puede ser negativo.")

    TAMANO_OPERACION = 1.0

    datos = Acargar_y_limpiar_csv.cargar_y_limpiar_csv(ruta_csv)
    if not datos:
        raise ValueError("No se encontraron filas validas en el CSV.")

    senales = Bgenerar_senales.generar_senales(datos)
    cuenta = CuentaDeTrading(saldo=saldo_inicial)

    posicion_abierta = None  # {'tipo': 'compra'/'venta', 'entrada': float, 'fecha': datetime, 'activo': str}

    for i, senal in enumerate(senales):
        if senal == "nada":
            continue

        vela = datos[i]
        precio_actual = vela["precio"]
        activo = vela.get("activo", "")
        fecha = vela["fecha"]

        # Abrir posicion si no hay una abierta
        if posicion_abierta is None:
            posicion_abierta = {
                "tipo": senal,
                "entrada": precio_actual,
                "fecha": fecha,
                "activo": activo,
            }
            continue

        # Si hay posicion y la senal es contraria, cerrar y abrir en la misma vela
        tipo_pos = posicion_abierta["tipo"]
        es_contraria = (tipo_pos == "compra" and senal == "venta") or (tipo_pos == "venta" and senal == "compra")
        if es_contraria:
            precio_entrada = posicion_abierta["entrada"]
            precio_salida = precio_actual

            if tipo_pos == "compra":
                resultado = (precio_salida - precio_entrada) * TAMANO_OPERACION
            else:  # venta abierta, se gana si baja
                resultado = (precio_entrada - precio_salida) * TAMANO_OPERACION

            cuenta.registrar_operacion(
                posicion_abierta["fecha"],
                posicion_abierta["activo"],
                tipo_pos,
                TAMANO_OPERACION,
                precio_entrada,
                precio_salida,
                resultado,
            )

            # Abrir la nueva posicion con la senal actual
            posicion_abierta = {
                "tipo": senal,
                "entrada": precio_actual,
                "fecha": fecha,
                "activo": activo,
            }

    # Cerrar al final si queda una posicion abierta
    if posicion_abierta is not None:
        ultima = datos[-1]
        precio_cierre = ultima["precio"]
        tipo_pos = posicion_abierta["tipo"]
        precio_entrada = posicion_abierta["entrada"]

        if tipo_pos == "compra":
            resultado = (precio_cierre - precio_entrada) * TAMANO_OPERACION
        else:
            resultado = (precio_entrada - precio_cierre) * TAMANO_OPERACION

        cuenta.registrar_operacion(
            posicion_abierta["fecha"],
            posicion_abierta["activo"],
            tipo_pos,
            TAMANO_OPERACION,
            precio_entrada,
            precio_cierre,
            resultado,
        )

    return cuenta


