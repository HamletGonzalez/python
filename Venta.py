#punto de venta
productos = [
    {'id':1, 'descripcion':'habichuela', 'precio':70},
    {'id':2, 'descripcion':'Arroz', 'precio':60},
    {'id':3, 'descripcion':'Pollo', 'precio':100},
    {'id':4, 'descripcion':'Aceite', 'precio':55},
    {'id':5, 'descripcion':'Lechuga', 'precio':25}
    ]

largo_id = 1
largo_descripcion = 1
largo_precio = 1

def imprimir_productos(productos):
    largo_id = 1 
    largo_descripcion = 1
    largo_precio = 1
    
    for item in productos:
        largo_id_actual = len(str(item['id']))
        largo_descripcion_actual = len(item['descripcion'])
        largo_precio_actual = len(str(item['precio']))
        if largo_id_actual > largo_id:
            largo_id = largo_id_actual
        if largo_descripcion_actual > largo_descripcion:
            largo_descripcion = largo_descripcion_actual
        if largo_precio_actual > largo_precio:
            largo_precio = largo_precio_actual
        largo_total = largo_id + largo_descripcion + largo_precio 
        largo_total = int(largo_total/2)-2
    print('-'*largo_total,'PRODUCTOS','-'*largo_total)
    for item in productos:
        print(item['id'],'.',item['descripcion'],item['precio'],'RD$')
        #print(item['id'],'-'*largo_id,{item:'descripcion'},'-'*largo_descripcion,{item:'precio'})
        
imprimir_productos(productos)

