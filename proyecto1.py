
class factura:
    def __init__(self,id,cliente,fecha,subtotal,total) :
        self.id = id
        self.cliente = cliente
        self.fecha = fecha
        self.subtotal = subtotal
        self.total = total
    
    def getid(self):
        return self.id 
    
    def getcliente(self):
        return self.cliente

    def getfecha(self):
        return self.fecha
    
    def getsubtotal(self):
        return self.subtotal
    
    def gettotal(self):
        return self.total
    
    def setid(self,new_id):
        self.id = new_id

    def setfecha(self,new_fecha):
        self.fecha = new_fecha

    def setsubtotal(self,new_subtotal):
        self.subtotal = new_subtotal

    def settotal(self,new_total):
        self.total = new_total

class articulo:
    def __init__(self,id,descripcion,cantidad_stock,precio,tipo_impuesto):
        self.id = id
        self.descripcion = descripcion
        self.cantidad_stock = cantidad_stock
        self.precio = precio
        self.tipo_impuesto = tipo_impuesto

    def getid(self):
        return self.id
    
    def getdescripcion(self):
        return self.descripcion
    
    def getcantidad(self):
        return self.cantidad_stock
    
    def getprecio(self):
        return self.precio
    
    def gettipo_impuesto(self):
        return self.tipo_impuesto
    
    def setcantidad(self,cantidad):
        self.cantidad_stock = cantidad
    
articulos = []
def menu(articulos):
    articulos.append(articulo(1,'GALLETAS',50,120,'00'))
    articulos.append(articulo(2,'JABON',20,100,'01'))
    articulos.append(articulo(3,'MANZANAS',35,15,'02'))
    articulos.append(articulo(4,'JUGO DE FRUTAS',20,215,'02'))
    articulos.append(articulo(5,'BOTELLA DE AGUA',20,225,'01'))

def imprimir_menu(articulos):
    menu(articulos)
    print('BIENVENIDO A LA SURTIDORA ITLA SANTIAGO SRL.','\n')
    print('---PRODUCTOS DISPONIBLES---')
    for item in articulos:
        print(item.getid(),'.',item.getdescripcion(),' ',item.getprecio(),'RD$')
    
imprimir_menu(articulos)

carrito = []
def llenar_carrito(carrito,articulos):
    id_articulo = 1
    cantidad_articulo = 0
    articulo_repetido = False
    articulo_existente = False
    print('\n','QUE DESEA LLEVAR?','\n','EN CASO DE QUERER TERMINAR LA COMPRA ELIGA EL CODIGO CERO (0) \n')
    while id_articulo != 0:
        id_articulo = int(input('INGRESE EL CODIGO DEL ARTICULO QUE DESEA: '))
        if id_articulo == 0:
            print('HA ELEGIDO TERMINAR LA COMPRA')
        else:
            for item in articulos:
                if item.getid() == id_articulo:
                    articulo_existente = True
                    if item.getcantidad() <= 0:
                        print('DEL ARTICULO SELECCIONADO (',item.getdescripcion(),') NO NOS QUEDAN UNIDADES')
                    else:
                        print('DEL ARTICULO SELECCIONADO TENEMOS ', item.getcantidad(),' UNIDADES' )
                        while cantidad_articulo <= 0 :
                            cantidad_articulo = int(input('CUANTAS DESEA? : '))
                            print('')
                            if cantidad_articulo <= 0 or cantidad_articulo > item.getcantidad():
                                print('LA CANTIDAD SELECCIONADA NO ES VALIDA')
                                cantidad_articulo = 0
                            else:
                                for items in carrito:
                                    if id_articulo == items['id_articulo']:
                                        articulo_repetido = True
                                        cantidad_anteriror = items['cantidad']
                                        items['cantidad'] = cantidad_anteriror + cantidad_articulo
                                        nueva_cantidad = item.getcantidad() - (cantidad_articulo )
                                        item.setcantidad(nueva_cantidad)
                                if articulo_repetido == False:
                                    carrito.append({'id_articulo':id_articulo,'cantidad':cantidad_articulo})
                                    nueva_cantidad = item.getcantidad() - cantidad_articulo
                                    item.setcantidad(nueva_cantidad)
            if articulo_existente == False:
                print('EL CODIGO DEL ARTICULO NO EXISTE \n')
            cantidad_articulo = 0
            articulo_repetido = False
            articulo_existente = False
llenar_carrito(carrito,articulos)
    
facturas = []
def imprimir_factura(carrito,facturas):
    cliente = input('A NOMBRE DE QUIEN ESTA HECHA LA COMPRA?  ')
    fecha = input('FECHA DE LA COMPRA (DD/MM/AAAA) ')
    id_factura = len(facturas) + 1
    subtotal = 0
    total = 0
    impuestos = 0
    largo_id = 1 
    largo_descripcion = 1
    largo_precio = 1
    largo_cantidad = 1
    largo_importe = 1

    for items in carrito:
        for item in articulos:
            if items['id_articulo'] == item.getid():
                subtotal = subtotal + (item.getprecio()*items['cantidad'])
                subtotal2 = item.getprecio()*items['cantidad']
                if item.gettipo_impuesto() == '01':
                    impuestos = impuestos + (subtotal2*0.18)
                elif item.gettipo_impuesto() == '02':
                    impuestos = impuestos + (subtotal2*0.16)
    total = subtotal + impuestos

    facturas.append(factura(id_factura,cliente,fecha,subtotal, total))
    
    for items in facturas:
        print('\n FACTURA #: ',items.getid(),'\n','CLIENTE : ',cliente,'\n','FECHA : ',fecha,'\n\n','DETALLES DE LA FACTURA: ')

    for item in articulos:
        largo_id_actual = len(str(item.getid()))
        largo_descripcion_actual = len(item.getdescripcion())
        largo_precio_actual = len(str(item.getprecio()))
        if largo_id_actual > largo_id:
            largo_id = largo_id_actual
        if largo_descripcion_actual > largo_descripcion:
            largo_descripcion = largo_descripcion_actual
        if largo_precio_actual > largo_precio:
            largo_precio = largo_precio_actual
    for item in carrito:
        largo_cantidad_actual = len(str(item['cantidad']))
        if largo_cantidad_actual > largo_cantidad:
            largo_cantidad = largo_cantidad_actual
        largo_importe_actual = len(str(item['cantidad']*largo_precio))
        if largo_importe_actual > largo_importe:
            largo_importe = largo_importe_actual
    print('ID','-'*(largo_id+2),'DESCRIPCION','-'*largo_descripcion,'PRECIO','-'*largo_precio,'CANTIDAD','-'*largo_cantidad,'IMPORTE')  

    for items in carrito:
        id_articulo = items['id_articulo']
        cantidad_articulo = items['cantidad']
        for items in articulos:
            if id_articulo == items.getid():
                descripcion_articulo = items.getdescripcion()
                precio_articulo = items.getprecio()
                importe = cantidad_articulo * precio_articulo
        print(id_articulo,' '*(largo_id+4-len(str(id_articulo))),descripcion_articulo,' '*(largo_descripcion+12-len(str(descripcion_articulo))), precio_articulo,' '*(largo_precio+7-len(str(precio_articulo))), cantidad_articulo,' '*(largo_cantidad+8-len(str(cantidad_articulo))), importe)

    #facturas[0].getsubtotal()
    print('\n TOTALES:\n','SUBTOTAL : ',facturas[0].getsubtotal(),'\n IMPUESTOS : ', impuestos, '\n TOTAL : ',facturas[0].gettotal())
    

if len(carrito) > 0:
    imprimir_factura(carrito,facturas)




