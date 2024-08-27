"""Escriba una función que reciba una lista de palabras y las devuelva organizadas 
alfabéticamente (necesitará crear al menos una función auxiliar).
 
NOTA: Si dos palabras comparten una o más letras iniciales debe verificar la 
siguiente letra hasta que se determine que una va primero que la otra. Por 
ejemplo: Campo va primero que cebolla, camión va primero que campo. 
Exclusivamente en este ejercicio puede utilizar .insert()"""


palabras = ['ejercicio','campo', 'camión','cebolla','iniciales']

def comparar_str(str1, str2):
    if str1 < str2:
        return True
    else :
        return False

def ordenar_alfabeticamente(palabras):
    total_palabras = len(palabras)
    for i in range(total_palabras):
        for x in range(0,total_palabras-i-1):
            if not comparar_str(palabras[x],palabras[x+1]):
                palabra1 = palabras[x]
                palabras[x] = palabras[x+1]
                palabras[x+1] = palabra1
    print(palabras)
ordenar_alfabeticamente(palabras)
            
    