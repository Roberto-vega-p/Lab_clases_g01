"""
Programación funcional con Python (POO)

Requisitos:
    - Solicitar al usuario 4 números por consola
    - Crear una función que devuelva cuál es el número mayor de los 4
      ingresados por el usuario
    - Finalmente asignar a una variable el valor de esta función
      para elevar al cubo este resultado y mostrarlo en la terminal
"""

# Solicitar al usuario 4 números por consola
def obtener_mayor_de_cuatro():
    pass  # Marcador de posición mientras defines la función

# Implementación de la función
def obtener_mayor_de_cuatro(n1, n2, n3, n4):
    return max(n1, n2, n3, n4)

# Solicitar los 4 números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

# Llamar a la función para obtener el mayor
numero_mayor = obtener_mayor_de_cuatro(num1, num2, num3, num4)

# Elevar al cubo el número mayor
resultado = numero_mayor ** 3

# Mostrar el resultado en la terminal
print(f"El número mayor es: {numero_mayor}")
print(f"El cubo del número mayor es: {resultado}")


