"""Uso del método random"""

import random

numero=random.randint(1,100)
print(numero)

mi_lista=[]

for elemento in range(10):
    #Le concedemos un valor aleatorio entre el 1 y 30
    elemento=random.randint(1,30)
    #Agregamos el numero aleatorio a la lista vacia
    mi_lista.append(elemento)

print("Mi lista actualizada tiene los siguientes valores: {}".format(mi_lista))

