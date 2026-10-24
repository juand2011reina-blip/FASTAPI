#comentario

#Variables
nombre = "Juan"
edad = 15
activo = True
valor = 150
valor = 200

if edad < 18 :
    print("Eres menor de edad")
elif edad <0 :
    print("No naces aún")
else:
    print("Eres mayor de edad")

edad = 20

if True:
    mensaje = "Hola"

print(mensaje)

lenguajes = ["Python", "JavaScript", "C++"]

for lenguaje in lenguajes:
    print(lenguaje)

persona = {
    "nombre": "Juan",
    "apellido": "Reina",
    "edad": 15
}

for numero in range(2,11,2):
    print(numero)

intentos = 0

while intentos < 3:
    intentos += 1
    print(f"Intento número: {intentos}")


lenguajes.append("C")
lenguajes[0]= "Typescript"

print(lenguajes[-1])

numeros = [10,20,30,40,50,60]
print(numeros[:4])

def saludar(a,b):
    return a+b

resultado = saludar(5,6)
print(resultado)

name = input("dime tu nombre: ")
print(name)

age = input("dime tu edad: ")
print(age)