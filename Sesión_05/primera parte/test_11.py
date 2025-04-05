"""Usando las propiedades de cadenas o string"""

"""
Requisitos:
 - Ingresar tu nombre y apellido por consola 
 (cada valor tiene que estar en una variable distinta)
 - Obtener el tamaño de tu nombre y apeellido completo luego de concatenarlos
 y mostrar en consola
 - Imprimir el resultado de la concatenación final todo en mayúsculas
 - Indicar mediante condicionales si el tamaño del nombre es mayor 
 o no al del apellido ingresado
 (Ingresar solo en este caso el apellido paterno)
 """
nombre=input("Ingresa tu nombre:")
apellidos=input("Ingresa tus apellidos completos:")
nombre_completo= nombre + " " + apellidos
print("Mi nombre completo es:"+nombre_completo)
tamaño_cadena=len(nombre_completo)
print("El tamaño de cadena es:",tamaño_cadena)

print("---------------------------------------------------------")
print("mi nombre completo en mayúscula es:{}".format(nombre_completo.upper()))

print("------------------------------------------------------------------")
apellido_paterno=input("Ingrese su apellido paterno:")
if  len(nombre) < len(apellido_paterno):
    print("El tamaño del nombre es menor que el tamaño del apellido paterno")
else:
    print("El tamaño del nombre es mayor que el tamaño del apellido paterno")



