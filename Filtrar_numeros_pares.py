""""Filtrar números pares: Dada una lista de números enteros, crea una función
llamada filter_even_numbers que tome esta lista como entrada y devuelva una
nueva lista que contenga solo los números pares."""

numeros = [1,2,3,4,5,6,7,8,9,10,11,12]

def filtro_par(x):
    if x%2 == 0:
        return True
    else:
        return False

def filter_even_numbers(numeros):
    pares = filter(filtro_par,numeros)
    print('lista de numeros enteros:')
    print(list(numeros))
    print('lista de numeros pares:')
    print(list(pares))
filter_even_numbers(numeros)