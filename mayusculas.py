"""Convertir cadenas a mayúsculas: Dada una lista de cadenas, crea una función
llamada uppercase_strings que tome esta lista como entrada y devuelva una nueva
lista donde todas las cadenas se conviertan a mayúsculas."""


palabras = ["Python", "es", "un", "lenguaje", "de", "programación"]

def uppercase_strings(palabras):
    x = lambda a : a.upper()
    
    palabras_upper = map(x,palabras)
    print(list(palabras_upper))
    
uppercase_strings(palabras)
    
    