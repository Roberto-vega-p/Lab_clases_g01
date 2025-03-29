"""
Requisitos

- Dentro de una empresa se va a solicitar pedir el
nombre y el apellido del empleado (input)
-Distrito de residencia y su sueldo actual (input)
- Sueldo y calculo del bono final del año, que será el triple del
 sueldo mensual menos el 10% del sueldo
 - Todos estos datos van a ingresar en un diccionario
 - Asignar a 3 variables usando asignación múltiple los valores del diccionario
 - Mostrar por la terminal el mensaje de : "Nombre" "apellido", "recibirá 'bono'
 soles de bono de fin de año"

"""
nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
dist_res=input("Ingrese su distrito residencia:")
suel_act=input("Ingrese su sueldo actual:")
bono_final=3*int(suel_act)-0.1*int(suel_act)

datos_empleado=dict(nombre=nombre,apellido=apellido,distrito_residencia=dist_res,sueldo_actual=int(suel_act),bono_final=bono_final)
print("Mi diccionario tiene el siguiente contenido:{} ".format(datos_empleado))

var_1, var_2, var_3, var_4, var_5=datos_empleado["nombre"],datos_empleado["apellido"],datos_empleado["distrito_residencia"],datos_empleado["sueldo_actual"],datos_empleado["bono_final"]
print("{} {}, recibirá {} soles de bono de fin de año".format(var_1,var_2,var_5))



