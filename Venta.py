#punto de venta
productos = [
    {'id':1, 'descripcion':'habichuela', 'precio':70},
    {'id':2, 'descripcion':'Arroz', 'precio':60},
    {'id':3, 'descripcion':'Pollo', 'precio':100},
    {'id':4, 'descripcion':'Aceite', 'precio':55},
    {'id':55, 'descripcion':'Lechuga', 'precio':25}
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
print('si desea salir eliga el codigo cero (0)') 

carrito = []


def llenar_carrito(productos):
    i = 0
    subtotal = 0
    encontrado = False
    codigo_existe = True
    codigo = 1
    cantidad_producto = 0
    while codigo_existe == True and codigo != 0:
        encontrado = False
        codigo_existe = False
        cantidad_producto = 0
        print('')
        #ingresar codigo
        codigo = int(input('coloque el codigo del producto que desea: '))
        if codigo == 0:
            print('\n','FIN DE LA COMPRA')    
        else :
            for item in productos:
                if codigo == item['id']:
                    codigo_existe = True
            if codigo_existe == True: #arreglar esta parte
                while cantidad_producto <= 0:
                    print('')
                    cantidad_producto = int(input('que cantidad desea? '))
                    if cantidad_producto <= 0:
                        print('La cantidad del producto tiene que ser mayor a cero','\n')
                if len(carrito) > 0:
                    for items in carrito:
                        if codigo == items['codigo'] :
                            encontrado = True
                            cantidad_anterior = items['cantidad_producto']
                            items['cantidad_producto']= cantidad_anterior + cantidad_producto
                    if encontrado == False:
                        carrito.append({'codigo': codigo,'cantidad_producto':cantidad_producto})
                        #codigo = 0
                elif encontrado == False:
                    carrito.append({'codigo': codigo,'cantidad_producto':cantidad_producto}) 
                    #codigo = 0            
            elif codigo_existe == False :
                print('el codigo colocado no existe')
                codigo_existe = True

llenar_carrito(productos)


def imprimiendo_factura(carrito,productos):
    largo_id = 1 
    largo_descripcion = 1
    largo_precio = 1
    largo_cantidad = 1
    largo_importe = 1
    subtotal = 0
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
        largo_cantidad_actual = len(str(item['cantidad_producto']))
        if largo_cantidad_actual > largo_cantidad:
            largo_cantidad = largo_cantidad_actual
        largo_importe_actual = len(str(item['cantidad_producto']*largo_precio))
        if largo_importe_actual > largo_importe:
            largo_importe = largo_importe_actual
    print('ID','-'*(largo_id+2),'DESCRIPCION','-'*largo_descripcion,'PRECIO','-'*largo_precio,'CANTIDAD','-'*largo_cantidad,'IMPORTE')  
    

    for item in carrito:
        codigo_producto = item['codigo']
        cant_producto = item['cantidad_producto']
        for items in productos:
            if codigo_producto == items['id']:
                descripcion_producto = items['descripcion']
                precio_producto = items['precio']        
        importe = cant_producto * precio_producto
        subtotal = subtotal + importe            
        print(codigo_producto,' '*(largo_id+4-len(str(codigo_producto))),descripcion_producto,' '*(largo_descripcion+12-len(str(descripcion_producto))), precio_producto,' '*(largo_precio+7-len(str(precio_producto))), cant_producto,' '*(largo_cantidad+8-len(str(cant_producto))), importe)
    print('\n','Totales de la compra:')
    print('Subtotal(sin itbis): ',subtotal)
    print('Impuestos: ',(subtotal*0.18)) 
    print('Total: ',subtotal+(subtotal*0.18))
    return
    """for i in range(0,len(carrito)):
        codigo_producto = carrito[i]['codigo']
        descripcion_producto = productos[{codigo_producto:'descripcion'}]
        precio_producto = productos[codigo_producto-1]['precio']
        cant_producto = carrito[i]['cantidad_producto']
        importe = cant_producto * precio_producto
        print(codigo_producto,' '*(largo_id+4-len(str(codigo_producto))),descripcion_producto,' '*(largo_descripcion+12-len(str(descripcion_producto))), precio_producto,' '*(largo_precio+7-len(str(precio_producto))), cant_producto,' '*(largo_cantidad+8-len(str(cant_producto))), importe)"""

if len(carrito) > 0 :
    imprimiendo_factura(carrito,productos)      