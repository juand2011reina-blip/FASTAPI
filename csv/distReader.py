import csv

with open("datos.csv", "r", encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)

    columnas = lector.fieldnames
    registros = list(lector)

print("Columnas:", columnas)
print("Cantidad de registros:", len(registros))
print("Primer registro:", registros[0] if registros else "No hay registros")