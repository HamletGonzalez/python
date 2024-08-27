
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
    articulos.append(articulo(4,'JUGO DE FRUTAS',20,225,'02'))
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
    print('\n','QUE DESEA LLEVAR?','\n','EN CASO DE QUERER SALIR DEL SISTEMA ELIGA EL CODIGO CERO (0) \n')
    while id_articulo != 0:
        id_articulo = int(input('INGRESE EL CODIGO DEL ARTICULO QUE DESEA: '))
        if id_articulo == 0:
            print('HA ELEGIDO SALIR DEL PROGRAMA')
        else:
            for item in articulos:
                if item.getid() == id_articulo:
                    articulo_existente = True
                    print('DEL ARTICULO SELECCIONADO TENEMOS ', item.getcantidad(),' UNIDADES' )
                    while cantidad_articulo <= 0 :
                        cantidad_articulo = int(input('CUANTAS DESEA? : '))
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
                print('EL CODIGO DEL ARTICULO NO EXISTE')
            cantidad_articulo = 0
            articulo_repetido = False
            articulo_existente = False
llenar_carrito(carrito,articulos)
    

