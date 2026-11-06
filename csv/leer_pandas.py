import pandas as pd
import numpy as np


ruta_csv = "Ventas.csv"
df = pd.read_csv(ruta_csv)

print("--- 1. CARGA EXITOSA ---")
print(f"Dataset cargado correctamente desde: {ruta_csv}\n")



print("--- 2. EXPLORACIÓN ---")


print("B) Primeros 5 registros:")
print(df.head(), "\n")


print("B) Dimensiones del DataFrame (Filas, Columnas):")
print(df.shape, "\n")


print("C) Lista de columnas:")
print(df.columns.tolist(), "\n")


print("D) Información general (info):")
df.info()
print("\n")


print("E) Resumen estadístico (describe):")
print(df.describe(), "\n")



print("--- 3. SELECCIÓN ---")

columnas_seleccionadas = df[['producto', 'ventas']]
print("A) Selección de dos columnas (producto y ventas):")
print(columnas_seleccionadas, "\n")


filtro_simple = df[df['ventas'] > 1000000]
print("B) Filtro con una condición (Ventas > 1,000,000):")
print(filtro_simple, "\n")

filtro_compuesto = df[(df['region'] == 'Norte') & (df['unidades'] >= 5)]
print("C) Filtro combinado (Región 'Norte' AND Unidades >= 5):")
print(filtro_compuesto, "\n")



print("--- 4. LIMPIEZA ---")


print("A) Valores faltantes por columna:")
print(df.isnull().sum(), "\n")



duplicados_totales = df.duplicated().sum()
print(f"B) Cantidad de registros completamente duplicados: {duplicados_totales}")
if duplicados_totales > 0:
    df = df.drop_duplicates()
    print("-> Registros duplicados eliminados.\n")
else:
    print("-> No se encontraron registros duplicados.\n")


print("--- 5. ANÁLISIS ---")

promedio_v = df['ventas'].mean()
minimo_v = df['ventas'].min()
maximo_v = df['ventas'].max()
total_v = df['ventas'].sum()

print(f"A) Estadísticas generales de la columna 'ventas':")
print(f"   - Promedio de ventas: ${promedio_v:,.2f}")
print(f"   - Venta mínima: ${minimo_v:,}")
print(f"   - Venta máxima: ${maximo_v:,}")
print(f"   - Total acumulado: ${total_v:,}\n")


print("B) Total de ventas agrupado por 'categoria':")
agrupado_cat = df.groupby('categoria')['ventas'].sum()
print(agrupado_cat, "\n")


print("--- 6. NUMPY ---")


arreglo_ventas = df['ventas'].to_numpy()
print("A) Columna 'ventas' convertida a arreglo de NumPy:")
print(arreglo_ventas, "\n")


iva_ventas = arreglo_ventas * 0.19
print("B) Operación vectorizada (Cálculo del 19% de IVA por registro):")
print(iva_ventas, "\n")


promedio_np = np.mean(arreglo_ventas)
mediana_np = np.median(arreglo_ventas)
desviacion_np = np.std(arreglo_ventas)

print("C) Métricas de ventas calculadas con NumPy:")
print(f"   - Promedio: ${promedio_np:,.2f}")
print(f"   - Mediana: ${mediana_np:,.2f}")
print(f"   - Desviación Estándar: ${desviacion_np:,.2f}\n")

print("--- FIN DEL ANALIZADOR ---")
