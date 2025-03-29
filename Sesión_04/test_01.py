"""Diccionario en Python"""

"""Los nombres de los key(llaves) van a ir escritos siempre en minusculas y 
sin tildes (por convecciòn o por buenas prácticas"""

var_1={"nombre":"Susana", "edad":29, "promedio": 14.9}

print("Mi diccionario tiene el siguiente contenido:{} ".format(var_1))

"""Agregamos el elemento con un nuevo key a mi diccionario"""

var_1["distrito"] = "Lince"
var_1["nombre"]="Roberto"
var_1["habilitado"]= True

print(var_1)

nombre=var_1["nombre"]
distrito=var_1["distrito"]
edad=var_1["edad"]

print(nombre,distrito,edad)









