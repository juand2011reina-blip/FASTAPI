from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(
    title="Mi Aplicación FastAPI",
    description="Esta es una aplicación de ejemplo en FastAPI con una API sencilla.",
    version="1.0.0"
)

# Modelo de datos para un producto
class Producto(BaseModel):
    nombre: str
    precio: float
    stock: int

# Base de datos simulada (lista de productos)
productos_db = [
    {"id": 1, "nombre": "Teclado inalámbrico", "precio": 10.99, "stock": 100},
    {"id": 2, "nombre": "Ratón óptico", "precio": 5.99, "stock": 200},
    {"id": 3, "nombre": "Monitor Full HD", "precio": 150.00, "stock": 50}
]

# 1. GET /: Mensaje de bienvenida o estado del servidor
@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {
        "mensaje": "¡Bienvenido a la API REST de Productos!",
        "estado": "Servidor activo y funcionando"
    }

# 2. GET /productos: Listar todos los productos
@app.get("/productos", response_model=List[Producto], status_code=status.HTTP_200_OK)
def listar_productos():
    return productos_db

# 3. GET /productos/{id}: Obtener un producto por su ID
@app.get("/productos/{id}", status_code=status.HTTP_200_OK)
def obtener_producto(id: int):
    for producto in productos_db:
        if producto["id"] == id:
            return producto
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Producto{id} no encontrado"
    )

# 4. POST /productos: Crear un nuevo producto
@app.post("/productos", status_code=status.HTTP_201_CREATED)
def crear_producto(producto: Producto):
    # Generar un ID automático autoincremental
    nuevo_id = productos_db[-1]["id"] + 1 if productos_db else 1
    
    nuevo_producto = {
        "id": nuevo_id,
        "nombre": producto.nombre,
        "precio": producto.precio,
        "stock": producto.stock
    }
    
    productos_db.append(nuevo_producto)
    return {
        "mensaje": "Producto registrado exitosamente",
        "producto": nuevo_producto
    }

# 5. DELETE /productos/{id}: Eliminar un producto
@app.delete("/productos/{id}", status_code=status.HTTP_200_OK)
def eliminar_producto(id: int):
    for index, producto in enumerate(productos_db):
        if producto["id"] == id:
            producto_eliminado = productos_db.pop(index)
            return {
                "mensaje": "Producto eliminado exitosamente",
                "producto": producto_eliminado
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No se pudo eliminar: el producto con ID {id} no existe."
    )

# Bloque para permitir ejecutar el servidor directamente con python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)