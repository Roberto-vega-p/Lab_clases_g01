"""
Requisitos
1. Crear 2 variables enteras,2 variables flotantes, 1 variable string (solamente caracteres),
1 variable string con contenido solamente numérico, 1 variable boolean
2. Obtener y mostrar la suma de una variable entera con la variable string numerica (realizar conversiones
si es necesario)
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica
y la variable flotante.
4. Obtener y mostrar el módulo de las variables enteras:%
5. Obtener y mostrar el resultado entero o la parte entera de las 2 variables int://
6. Obtener la potencia usando una de las variables flotantes como base y la variable entera como potencia.
"""
a=3
b=5
c=3.1
bb=5.2
d="string"
e="10"
f=True
suma_1=a+int(e)
suma_2= a+b+int(e)+bb
modulo=a%b
cocent=a//b
pot=pow(bb,a)

print("suma_1={}".format(suma_1))
print("suma_2={}".format(suma_2))
print("modulo={}".format(modulo))
print("cocent={}".format(cocent))
print("pot={}".format(pot))