menu=[{'id':15959, 'nombre':'Arroz', 'precio':50},
      {'id':2, 'nombre':'Habichuelas', 'precio':80},
      {'id':3, 'nombre':'Aceite', 'precio':300},
      {'id':4, 'nombre':'Pollo', 'precio':85},
      {'id':123452123, 'nombre':'Lechuga', 'precio':80},]

carrito=[]

def imprimir_menu(menu):
    tammax=0
    for item in menu:
        tamactual=len(str(item['id']))+len(item['nombre'])+len(str(item['precio']))
        if  tamactual>tammax:
            tammax=tamactual
    print('-'*(int(tammax/2+2))+'Menú'+'-'*(int(tammax/2+2)))
    for item in menu:
        print(f'{item['id']}. {item['nombre']} -> RD${item['precio']}')