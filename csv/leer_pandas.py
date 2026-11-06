import pandas as pd
import numpy as np

ruta_csv = "ventas.csv"
df = pd.read_csv(ruta_csv)

print("--- 1. CARGA EXITOSA ---")
print(f"Dataset cargado correctamente desde: {ruta_csv}\n")


print("--- 2. EXPLORACIÓN ---")


print("A) Primeros 5 registros:")
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
print("A) Selección de dos columnas:")
print(columnas_seleccionadas.head(), "\n")

filtro_simple = df[df['ventas'] > 100]
print("B) Filtro con una condición (Ventas > 100):")
print(filtro_simple.head(), "\n")


filtro_compuesto = df[(df['ventas'] > 100) & (df['cantidad'] > 2)]
print("C) Filtro combinado (Ventas > 100 AND Cantidad > 2):")
print(filtro_compuesto.head(), "\n")


print("--- 4. LIMPIEZA ---")


print("A) Valores faltantes por columna antes de la limpieza:")
print(df.isnull().sum(), "\n")


if df['ventas'].isnull().sum() > 0:
    mediana_ventas = df['ventas'].median()
    df['ventas'] = df['ventas'].fillna(mediana_ventas)
    print(f"-> Se reemplazaron los nulos de 'ventas' con la mediana: {mediana_ventas}")


duplicados_totales = df.duplicated().sum()
print(f"B) Cantidad de registros completamente duplicados detectados: {duplicados_totales}")

if duplicados_totales > 0:
    df = df.drop_duplicates()
    print("-> Registros duplicados eliminados con éxito.\n")
else:
    print("-> No se requirió eliminación de duplicados.\n")



print("--- 5. ANÁLISIS ---")


promedio = df['ventas'].mean()
minimo = df['ventas'].min()
maximo = df['ventas'].max()
total = df['ventas'].sum()

print(f"A) Estadísticas de la columna 'ventas':")
print(f"   - Promedio: {promedio:.2f}")
print(f"   - Mínimo: {minimo}")
print(f"   - Máximo: {maximo}")
print(f"   - Total acumulado: {total}\n")


print("B) Agrupación por 'categoria' y su precio promedio:")
agrupado = df.groupby('categoria')['ventas'].mean()
print(agrupado, "\n")


print("--- 6. NUMPY ---")

arreglo_ventas = df['ventas'].to_numpy()
print("A) Columna convertida a arreglo de NumPy (primeros 5 elementos):")
print(arreglo_ventas[:5], "\n")

ventas_con_impuesto = arreglo_ventas * 1.16
print("B) Operación vectorizada (Ventas con 16% de impuesto - primeros 5):")
print(ventas_con_impuesto[:5], "\n")

promedio_np = np.mean(arreglo_ventas)
mediana_np = np.median(arreglo_ventas)
desviacion_np = np.std(arreglo_ventas)

print("C) Métricas calculadas con NumPy:")
print(f"   - Promedio (NumPy): {promedio_np:.2f}")
print(f"   - Mediana (NumPy): {mediana_np:.2f}")
print(f"   - Desviación Estándar (NumPy): {desviacion_np:.2f}\n")

print("--- FIN DEL ANALIZADOR ---")
