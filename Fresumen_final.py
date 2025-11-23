from Dsimulador_ejecucion import ejecutar_trading


def pedir_float(prompt: str) -> float:
    while True:
        valor = input(prompt).strip()
        try:
            saldo = float(valor)
            if saldo < 0:
                print("Introduce un saldo no negativo.")
                continue
            return saldo
        except ValueError:
            print("Valor no valido. Introduce un numero (ej. 1000 o 1000.0).")


def pedir_int_opcional(prompt: str) -> int | None:
    while True:
        valor = input(prompt).strip()
        if valor == "":
            return None
        try:
            numero = int(valor)
            if numero <= 0:
                print("Introduce un entero positivo o deja vacio para usar todas las operaciones.")
                continue
            return numero
        except ValueError:
            print("Valor no valido. Introduce un entero positivo o deja vacio.")


def imprimir_resumen(cuenta, saldo_inicial: float) -> None:
    ops = cuenta.historial_operaciones
    total = len(ops)
    ganadoras = sum(1 for op in ops if op.get("resultado", 0) > 0)
    perdedoras = sum(1 for op in ops if op.get("resultado", 0) < 0)
    beneficio_total = cuenta.saldo - saldo_inicial

    print("\nResumen del backtest")
    print("--------------------")
    print(f"Saldo inicial: {saldo_inicial}")
    print(f"Saldo final:   {cuenta.saldo}")
    print(f"Numero de operaciones: {total}")
    print(f"Ganadoras: {ganadoras}")
    print(f"Perdedoras: {perdedoras}")
    print(f"Beneficio total: {beneficio_total}")

    print("\nOperaciones registradas:")
    for op in ops:
        fecha = op.get("fecha")
        fecha_cierre = op.get("fecha_cierre", fecha)
        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S") if hasattr(fecha, "strftime") else str(fecha)
        fecha_cierre_str = (
            fecha_cierre.strftime("%Y-%m-%d %H:%M:%S") if hasattr(fecha_cierre, "strftime") else str(fecha_cierre)
        )
        instrumento = op.get("instrumento", "")
        tipo = op.get("tipo", "")
        direccion = "alcista" if tipo == "compra" else "bajista" if tipo == "venta" else tipo
        tamano = op.get("tamano", op.get("tamaño", 1.0))
        entrada = op.get("precio_entrada")
        salida = op.get("precio_salida")
        resultado = op.get("resultado")
        print(f"{fecha_str} | Abre operacion {direccion} | {instrumento} | size={tamano} | entrada={entrada}")
        print(f"{fecha_cierre_str} | Cierra operacion {direccion} | {instrumento} | salida={salida} | pnl={resultado}")


def main() -> None:
    print("=== Simulador de trading ===")
    saldo_inicial = pedir_float("Introduce el saldo inicial: ")
    max_ops = pedir_int_opcional("Numero de operaciones a simular (vaciar para todas): ")

    ruta_csv = "precios.csv"
    cuenta = ejecutar_trading(ruta_csv, saldo_inicial=saldo_inicial, max_operaciones=max_ops)
    imprimir_resumen(cuenta, saldo_inicial)


if __name__ == "__main__":
    main()
