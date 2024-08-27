"""Utilizando map, lambda y/o filter, escriba una función que reciba un arreglo de 
números y devuelva un arreglo solo con números los números que sean 
tartamudos. 
NOTA: Un número de cuatro cifras es tartamudo si tiene las dos primeras cifras 
iguales entre sí y las dos últimas cifras iguales entre sí, por ejemplo 3311 y 
2222 son números tartamudos."""


numeros = ['1230','1451','4488','1212','2244','6622']

def buscar_tartamudos(x):
    if x[0] == x[1] and x[2] == x[3]:
        return True
    else:
        return False
        
def numeros_tartamudos(numeros):
    tartamudos = filter(buscar_tartamudos,numeros)
    print(list(tartamudos))
        
numeros_tartamudos(numeros)


