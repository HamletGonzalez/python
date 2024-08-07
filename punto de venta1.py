

#punto de venta
productos = [
    {'id':1, 'descripcion':'habichuela', 'precio':70},
    {'id':2, 'descripcion':'Arroz     ', 'precio':60},
    {'id':3, 'descripcion':'Pollo     ', 'precio':100},
    {'id':4, 'descripcion':'Aceite    ', 'precio':55},
    {'id':5, 'descripcion':'Lechuga   ', 'precio':25}
    ]

#imprimiendo los productos disponibles
print('bienvenido a este punto de venta, que productos desea llevar?','\n')
cant_productos = len(productos)
for i in range(0,cant_productos):
    print(productos[i]['id'],'.',productos[i]['descripcion'],'RD$',productos[i]['precio'])

#imprimiendo los productos en forma de menu