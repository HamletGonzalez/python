"""Calcular el cuadrado de los números positivos: Dada una lista de números enteros,
crea una función llamada square_positive_numbers que tome esta lista como
entrada y devuelva una nueva lista que contenga los cuadrados de los números
positivos."""


numeros = [-100, -75, -50, -25, 0, 25, 50, 75, 100]

def filtro_positivo(x):
    if x <= 0:
        return False
    else:
        return True
    
def square_positive_numbers(numeros):
    x = lambda a : a*a
    cuadrado = filter(filtro_positivo, numeros)
    cuadrado = map(x,cuadrado)
    print('lista de numeros original:')
    print(numeros)
    print('lista de numeros positivos y al cuadrado de la lista:')
    print(list(cuadrado))
square_positive_numbers(numeros)
    