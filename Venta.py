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


print('\n','bienvenido a este punto de venta, que productos desea llevar?','\n')
print('si desea salir eliga el codigo cero (0)','\n') 

carrito = []


def llenar_carrito(productos):
    i = 0
    subtotal = 0
    encontrado = False
    codigo = 1
    cantidad_producto = 0
    while codigo != 0:
        encontrado = False
        cantidad_producto = 0
        numero_productos = len(productos)
        #ingresar codigo
        codigo = int(input('coloque el codigo del producto que desea: '))
        if codigo == 0:
            print("\n",'datos de la compra-->',"\n")
        elif codigo in range(0,numero_productos+1):#
            while cantidad_producto <= 0:
                descripcion = productos[codigo-1]['descripcion']
                print('\n','que cantidad de', descripcion, ' desea?')
                cantidad_producto = int(input(''))
                if cantidad_producto <= 0:
                    print('La cantidad del producto tiene que ser mayor a cero','\n')
            total_producto = productos[codigo-1]['precio'] * cantidad_producto
            subtotal = subtotal + total_producto            
            if len(carrito) > 0:
                for items in carrito:
                    if codigo == items['codigo'] :
                        encontrado = True
                        cantidad_anterior = items['cantidad_producto']
                        items['cantidad_producto']= cantidad_anterior + cantidad_producto
                if encontrado == False:
                    carrito.append({'codigo': codigo,'cantidad_producto':cantidad_producto})
            elif encontrado == False:
                carrito.append({'codigo': codigo,'cantidad_producto':cantidad_producto})             
        else :
                print('el codigo colocado no existe','\n')

llenar_carrito(productos)


def imprimiendo_factura(carrito,productos):
    largo_id = 1 
    largo_descripcion = 1
    largo_precio = 1
    print('detalle de la compra: ')
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
    for item in carrito:
        largo_cantidad = 1
        largo_importe = 1
        largo_cantidad_actual = len(str(item['cantidad_producto']))
        if largo_cantidad_actual > largo_cantidad:
            largo_cantidad = largo_cantidad_actual
        largo_importe_actual = len(str(item['cantidad_producto']*largo_precio))
        if largo_importe_actual > largo_importe:
            largo_importe = largo_importe_actual
    print('ID','-'*(largo_id+2),'DESCRIPCION','-'*largo_descripcion,'PRECIO','-'*largo_precio,'CANTIDAD','-'*largo_cantidad,'IMPORTE')  
    
    for i in range(0,len(carrito)):
        codigo_producto = carrito[i]['codigo']
        descripcion_producto = productos[codigo_producto-1]['descripcion']
        precio_producto = productos[codigo_producto-1]['precio']
        cant_producto = carrito[i]['cantidad_producto']
        importe = cant_producto * precio_producto
        print(codigo_producto,' '*(largo_id+4-len(str(codigo_producto))),descripcion_producto,' '*(largo_descripcion+12-len(str(descripcion_producto))), precio_producto,' '*(largo_precio+7-len(str(precio_producto))), cant_producto,' '*(largo_cantidad+8-len(str(cant_producto))), importe)


    
imprimiendo_factura(carrito,productos)      