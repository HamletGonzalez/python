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
            print("\n",'datos de la compra:',"\n")
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
                    if codigo == carrito[items]['codigo'] :
                        encontrado = True
                        cantidad_anterior = carrito[items]['cantidad_producto']
                        carrito[items]['cantidad_producto']= cantidad_anterior + cantidad_producto
                if encontrado == False:
                    carrito.append({'codigo': codigo,'cantidad_producto':cantidad_producto})
            elif encontrado == False:
                carrito.append({'codigo': codigo,'cantidad_producto':cantidad_producto})             
        else :
                print('el codigo colocado no existe','\n')

llenar_carrito(productos)