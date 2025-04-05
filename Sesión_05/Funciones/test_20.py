"""
Programación funcional con Python (POO)

Requisitos:
    - Crear una función que multiplicará 3 valores y luego restará el segundo parámetro
    - Para esta función el tercer parámetro contendrá un valor
    - Mostrar 2 casos donde se ingrese los valores donde uno no afectará
    el valor del parámetro que ya contiene un valor
    y otro donde si lo estará afectando
"""
def funcaritm (a,b,c=10):
        return a*b*c-b

var_1,var_2,var_3=2,3,4

resultado_1=funcaritm(var_1,var_2,var_3)
print(resultado_1)

resultado_2=funcaritm(var_1,var_2)
print(resultado_2)
