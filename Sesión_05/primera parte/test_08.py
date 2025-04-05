"""if ternarios"""

"""
Requisitos: 
 - Ingresar por teclado el sueldo de un empleado
 - Si el sueldo es mayor a 2500 y menor a 3500, imprimir "Su sueldo no tiene bonificación"
 y se le agregará el 10%, para luego mostrar el sueldo final con la bonificación
 - Caso contrario: "Su sueldo tiene bonificación este año y será de: 
 'sueldo_final'", sueldo_final= sueldo + 2% sueldo
"""
# Solicitar el sueldo del empleado
sueldo = float(input("Ingrese el sueldo del empleado: "))

# Usar un operador ternario para determinar el sueldo final
sueldo_final = sueldo + (0.10 * sueldo) if 2500 < sueldo < 3500 else sueldo + (2 * sueldo)

# Imprimir el resultado según la condición
mensaje = "Su sueldo no tiene bonificación. Su sueldo final con la bonificación es: " + str(sueldo_final) \
    if 2500 < sueldo < 3500 else "Su sueldo tiene bonificación este año y será de: " + str(sueldo_final)

print(mensaje)