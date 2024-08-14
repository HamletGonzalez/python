"""Filtrar nombres que comienzan con 'A': Dada una lista de nombres, crea una
función llamada filter_names_starting_with_a que tome esta lista como entrada y
devuelva una nueva lista que contenga solo los nombres que comiencen con la
letra 'A'."""


nombres = ["Ariel", "Mateo", "Valentina", "Benjamín", "Emma", "Lucas", "Olivia", "Daniel", "Aurora"]

def nombres_con_a(x):
    if x[0].lower() == 'a':
        return True
    else: 
        return False

def filter_names_starting_with_a(nombres):
    names_starting_with_a = filter(nombres_con_a,nombres)
    print('lista de nombres:')
    print(nombres)
    print('lista de nombres que comienzan con a:')
    print(list(names_starting_with_a))
filter_names_starting_with_a(nombres)