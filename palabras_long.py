"""Filtrar palabras con longitud mayor a 5: Dada una lista de palabras, crea una
función llamada filter_long_words que tome esta lista como entrada y devuelva
una nueva lista que contenga solo aquellas palabras con una longitud mayor a 5
caracteres."""

palabras = ["Python", "es", "un", "lenguaje", "de", "programación"]

def filtro_longitud(x):
    if len(x) < 5:
        return False
    else:
        return True

def filter_long_words(palabras):
    long_words = filter(filtro_longitud,palabras)
    print('palabras de la lista original:')
    print(palabras)
    print('palabras con una longitud mayor a 5 de la lista:')
    print(list(long_words))
    
filter_long_words(palabras)