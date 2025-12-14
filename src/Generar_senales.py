import mini_trading_simulator.Cargar_y_limpiar_csv as Cargar_y_limpiar_csv

def generar_senales(datos):
    senales = []

    for i, fila in enumerate(datos):
        if i<3:
            senales.append("nada")
            continue
        
        precios_recientes = [p["precio"] for p in datos[i-3:i]]
        media = sum(precios_recientes) / 3

        precio_actual = fila["precio"]

        if precio_actual < media:
            senales.append("compra")
        elif precio_actual > media:
            senales.append("venta")
        else:
            senales.append("nada")

    return senales