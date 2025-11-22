import csv
from datetime import datetime


def cargar_csv(ruta):
    
    limpios = []

    with open(ruta, newline="",encoding='utf-8') as f:
        lector = csv.Dictreader(f)
        for fila in datos:
            if all((v is None or str(v).strip()=="") for v in filas.values()):
            continue
            
            try:
                nueva = dict(fila)
                nueva["precio"] = float(str(fila["precio"]).replace(',','.'))
                nueva['fecha'] = datetime.fromisoformat(str(fila['fecha']).strip())
        
            except(KeyError,ValueError,TypeError):
                continue

            limpios.append(nueva)

    return limpios
