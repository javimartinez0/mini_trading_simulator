import csv
from datetime import datetime


def cargar_y_limpiar_csv(ruta):

    limpios = []

    with open(ruta, newline="",encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            if all((v is None or str(v).strip()=="") for v in fila.values()):
                    continue
            try:
                nueva = dict(fila)
                nueva["precio"] = float(str(fila["precio"]).replace(',','.'))
                nueva['fecha'] = datetime.fromisoformat(str(fila['fecha']).strip())
        
            except(KeyError,ValueError,TypeError):
                    continue

            limpios.append(nueva)

    return limpios

