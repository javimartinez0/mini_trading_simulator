import Acargar_y_limpiar_csv
import os

def generar_señales(datos):
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

BASE = os.path.dirname(__file__)
datos = Acargar_y_limpiar_csv.cargar_y_limpiar_csv(os.path.join(BASE,"precios.csv"))
senales = generar_señales(datos)
print(senales)

print(os.path.abspath("precios.csv"))