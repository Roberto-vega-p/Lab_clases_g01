"""Listas en Python"""

"""Listas -> del: Eliminarà un valor indicando el ìndice del valor de la lista"""

paises=[]

paises.append("Perú")
paises.append("Brasil")
paises.append("Argentina")
paises.append("Cánada")
paises.append("Mexico")
paises.append("Guatemala")

print(paises)

del paises[2]

print("Milista actualizada tiene estos valores: {}".format(paises))

del paises[4]

print("Milista actualizada tiene estos valores: {}".format(paises))


