""""Doble todos los números en una lista: Dada una lista de números enteros, crea
una función llamada double_numbers que tome esta lista como entrada y devuelva
una nueva lista donde cada número se haya duplicado."""

numeros = [1,2,3,4,5,6,7,8,9,10,11,12]

def double_numbers(numeros):
    x = lambda a : a*2
    numeros_duplicados = map(x,numeros)
    print('lista anterior:')
    print(numeros)
    print('lista nueva:')
    print(list(numeros_duplicados))

double_numbers(numeros)
    