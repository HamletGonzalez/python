

#punto de venta
productos = [
    {'id':1, 'descripcion':'habichuela', 'precio':70},
    {'id':2, 'descripcion':'Arroz     ', 'precio':60},
    {'id':3, 'descripcion':'Pollo     ', 'precio':100},
    {'id':4, 'descripcion':'Aceite    ', 'precio':55},
    {'id':5, 'descripcion':'Lechuga   ', 'precio':25}
    ]

largo_id = 1
largo_descripcion = 1
largo_precio = 1

def imprimir_productos(productos):
    for item in productos:
        largo_id_actual = len({item:'id'})
        largo_descripcion_actual = len({item:'descripcion'})
        largo_precio_actual = len({item:'precio'})
        if largo_id_actual > largo_id:
            largo_id = largo_id_actual
        if largo_descripcion_actual > largo_descripcion:
            largo_descripcion = largo_descripcion_actual
        if largo_precio_actual > largo_precio:
            largo_precio = largo_precio_actual 
    for item in productos:
        print({item:'id'},'-'*largo_id,{item:'descripcion'},'-'*largo_descripcion,{item:'precio'})
        
imprimir_productos(productos)

#imprimiendo los productos disponibles
print('bienvenido a este punto de venta, que productos desea llevar?','\n')
cant_productos = len(productos)
for i in range(0,cant_productos):
    print(productos[i]['id'],'.',productos[i]['descripcion'],'RD$',productos[i]['precio'])
print('bienvenido a este punto de venta, que productos desea llevar?','\n')
print('si desea salir eliga el codigo cero (0)','\n')

#inicializo las variables para el proceso de agregar productos al carrito
subtotal = 0
encontrado = False
carrito = []
cantidad_producto = 0
codigo = 1
i = 0

while codigo != 0:
    encontrado = False
    cantidad_producto = 0
    #ingresar codigo
    codigo = int(input('coloque el codigo del producto que desea: '))
    if codigo == 0:
        print("\n",'datos de la compra:',"\n")
    elif codigo in range(0,cant_productos+1):
        while cantidad_producto <= 0:
            descripcion = productos[codigo-1]['descripcion']
            print('\n','que cantidad de', descripcion, ' desea?')
            cantidad_producto = int(input(''))
            if cantidad_producto <= 0:
                print('La cantidad del producto tiene que ser mayor a cero','\n')
        total_producto = productos[codigo-1]['precio'] * cantidad_producto
        subtotal = subtotal + total_producto            
        if len(carrito) > 0:
            for i in range(0,len(carrito)):
                if codigo == carrito[i]['codigo'] :
                    encontrado = True
                    cantidad_anterior = carrito[i]['cantidad_producto']
                    carrito[i]['cantidad_producto']= cantidad_anterior + cantidad_producto

            if encontrado == False:
                carrito.append({'codigo': codigo,'cantidad_producto':cantidad_producto})

        elif encontrado == False:
            carrito.append({'codigo': codigo,'cantidad_producto':cantidad_producto})             
    else :
            print('el codigo colocado no existe','\n')
            
#imprimiendo los datos de la compra
print('detalle de la compra: ')
print('ID -- DESCRIPCION -- PRECIO -- CANTIDAD -- IMPORTE')

i = 0
productos_en_carrito = len(carrito)
for i in range(0,productos_en_carrito):
    codigo_producto = carrito[i]['codigo']
    descripcion_producto = productos[codigo_producto-1]['descripcion']
    precio_producto = productos[codigo_producto-1]['precio']
    cant_producto = carrito[i]['cantidad_producto']
    importe = cant_producto * precio_producto

    print(codigo_producto,'   ', descripcion_producto,'     ', precio_producto,'         ', cant_producto,'     ', importe)

print('\n','Totales de la compra:')
print('Subtotal(sin itbis): ',subtotal)
print('Impuestos: ',(subtotal*0.18)) 
print('Total: ',subtotal+(subtotal*0.18))         