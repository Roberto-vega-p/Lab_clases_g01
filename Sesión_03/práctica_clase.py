var_1=[]
var_2=[]
var_1.append("Juan")
var_1.append(30)
var_1.append("ing. agroindustrial")
var_2.append("Luis")
var_2.append(35)
var_2.append("ing. sistemas")

print("1-------------------------------------")
suma_edad=var_1[1] + var_2[1]
print("la suma de edades es:{}".format(suma_edad))

print("2--------------------------------------")
suma_listas=var_1+var_2
print("la suma_listas es:{}".format(suma_listas))

print("3---------------------------------------")
suma_listas.reverse()
print("la lista actualizada de suma_listas es:{}".format(suma_listas))

print("4-----------------------------------------")

suma_listas.remove(35)
print("la lista actualizada de suma_listas es:{}".format(suma_listas))

suma_listas.remove(30)
print("la lista actualizada de suma_listas es:{}".format(suma_listas))

print("5----------------------------------------------------------------")
var_2.clear()
print("la lista actualizada de var_2 es:{}".format(var_2))



