"""
Requisitos

1. Crear variables para los valores de nombre, profesión y ciudad
2. Crear 2 variables para la remuneración de enero y febrero
3. Crear 1 variable donde se sumara el ingreso de los meses de enero y febrero
4. Mostrar en pantalla el mensaje de:
"Hola soy 'nombre' mi 'profesion' y mi remuneración acumulada es de 'remuneración total'"
"""
nombre="Roberto Vega"
profesion='ing. agroindustrial'
ciudad= 'Lima'
remun_enero=1000
remun_febrero=1200
remun_total=remun_enero + remun_febrero
print("Hola, soy {} de la ciudad {}, mi profesion es {} y mi remuneración acumulada es de {}".format(nombre,ciudad, profesion, remun_total))
