"""Escriba una función que reciba dos matrices cuadradas, A y B, y devuelva la suma 
de A y transposición de B. Debe manejar la posibilidad de que reciba matrices con 
dimensiones diferentes. 
NOTA: Una matriz transpuesta es una matriz obtenida al intercambiar sus filas 
por columnas, de manera que las entradas que estaban en las filas pasan a 
estar en las columnas y viceversa"""


a =         [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

b = [[10, 11, 12,20],
           [13, 14, 15,21],
           [16, 17, 18,22],
           [30,31,32,33]]

if len(a) != len(b):
    print('las matrices no cuentan con las mismas dimensiones')

def matriz(b):
    transposicion = []
    for items in range(len(b[0])):
        fila = []
        for i in range(len(b)):
            fila.append(b[i][items])    
        transposicion.append(fila)
    #print(list(transposicion))
    return transposicion
matriz(b)

def suma_matriz(a,b):
    transpuesta = matriz(b)

    matriz_suma = []
    for i in range(len(a)):
        fila=[]
        for x in range(len(a[0])):
            fila.append(a[i][x] + transpuesta[i][x])
        matriz_suma.append(fila)
    print(list(matriz_suma))
suma_matriz(a,b)