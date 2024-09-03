import os

class almacen:
    def __init__(self,id,nombre,volumen_total,volumen_dis,items) :
        self.id = id
        self.nombre = nombre
        self.volumen_total = volumen_total
        self.volumen_dis = volumen_dis
        self.items = items
        
    def getid(self): 
        return self.id
    
    def getnombre(self):
        return self.nombre
    
    def getvolumen_total(self):
        return self.volumen_total
    
    def getvolumen_dis(self):
        return self.volumen_dis
    
    def getitems(self):
        return self.items
    
    def setitems(self,new_items):
        self.items = new_items
    
class item:
    def __init__(self,id,descripcion,volumen,almacen_desig) :
        self.id = id
        self.descripcion = descripcion
        self.volumen = volumen
        self.almacen_desig = almacen_desig
        
    def getid(self):
        return self.id 

    def getdescripcion(self):
        return self.descripcion
    
    def getvolumen(self):
        return self.volumen 
    
    def getalmacen_desig(self):
        return self.almacen_desig
            

almacenes = []
items = []

def llenar_items(items):
    items.append(item(1,'SECADORA',40,1))
    items.append(item(2,'MESA',50,2))
    items.append(item(3,'SILLAS',60,2))
    items.append(item(4,'TELAS',20,0))
    items.append(item(521,'NEUMATICOS',80,0))
    
def llenar_almacenes(almacenes):
    almacenes.append(almacen(1,'BODEGA DE MATERIALES',250,160,[{'id_item':1,'volumen_item':40}]))
    almacen_extra = [
        {'id_item':2,'volumen_item':50},
        {'id_item':3,'volumen_item':60}
        ]
    almacenes.append(almacen(2,'ALMACEN CENTRAL',500,290,almacen_extra))


llenar_items(items)
llenar_almacenes(almacenes)

def registrar_item(items):
    almacen_encontrado = False
    id_item = len(items) + 1
    descripion = input('INGRESE LA DESCRIPCION DEL ITEM A REGISTRAR : ')
    volumen = int(input('INGRESE EL VOLUMEN (M3) DEL ARTICULO : '))
    almacen = int(input('INGRESE EL ID DEL ALMACEN DEL ARTICULO : '))
    for x in almacenes:
        if x.getid() == almacen:
            almacen_encontrado = True
            volumen_dis = x.getvolumen_dis()
            if (x.getvolumen_dis() - volumen) < (x.getvolumen_total()*0.2):
                print('EL VOLUMEN DEL ITEM ES MAYOR A LO PERMITIDO EN ESTE ALMACEN')
                almacen_encontrado = False
    if almacen_encontrado == True:
        items.append(item(id_item,descripion,volumen,almacen))
        print('EL ITEM FUE REGISTRADO CON EXITO')
    else:   
        print('EL ITEM NO PUDO SER REGISTRADO ')

def registrar_almacen(almacenes):
    id_almacen = len(almacenes) + 1
    descripion = input('INGRESE LA DESCRIPCION DEL ALMACEN A REGISTRAR : ')
    volumen = int(input('INGRESE LA CAPACIDAD MAXIMA O VOLUMEN(M3) DEL ALMACEN : '))
    volumen_dis = volumen - (volumen*0.2)
    almacenes.append(almacen(id_almacen,descripion,volumen,volumen_dis,[]))

def listar_items(items,almacenes):
    print('---LISTADO DE ITEMS---')
    largo_id = 1 
    largo_descripcion = 1
    largo_volumen = 1
    largo_id_almacen = 1
    largo_almacen = 1
    for x in items:
        largo_id_actual = len(str(x.getid()))
        largo_descripcion_actual = len(x.getdescripcion())
        largo_volumen_actual = len(str(x.getvolumen()))
        largo_id_almacen_act = len(str(x.getalmacen_desig()))
        if largo_id_actual > largo_id:
            largo_id = largo_id_actual
        if largo_descripcion_actual > largo_descripcion:
            largo_descripcion = largo_descripcion_actual
        if largo_volumen_actual > largo_volumen:
            largo_volumen = largo_volumen_actual
        if largo_id_almacen_act > largo_id_almacen:
            largo_id_almacen = largo_id_almacen_act
    for i in almacenes:
        largo_almacen_act = len(i.getnombre())
        if largo_almacen_act > largo_almacen:
            largo_almacen = largo_almacen_act
    print('ID','-'*(largo_id+2),'DESCRIPCION','-'*(largo_descripcion),'VOLUMEN(M3)','-'*largo_volumen,'ALMACEN','-'*largo_id_almacen,'NOMBRE ALMACEN')

    almacen_encontrado = False
    #print('---LISTADO DE ITEMS---')
    for x  in items:
        almacen_encontrado = False
        id_item = x.getid()
        descripcion = x.getdescripcion()
        volumen = x.getvolumen()
        almacen = x.getalmacen_desig()
        for i in almacenes:
            if almacen == i.getid():
                almacen_encontrado = True
                nombre_almacen = i.getnombre()
        if almacen_encontrado == False:
            nombre_almacen = ''
        print(id_item,' '*(largo_id+4-len(str(id_item))),descripcion,' '*(largo_descripcion+11-len(descripcion)),volumen,' '*(largo_volumen+11-len(str(volumen))),almacen,' '*(largo_id_almacen+7-len(str(almacen))), nombre_almacen,)

def listar_almacenes(almacenes):
    print('---LISTADO DE ALMACENES---')
    for x in almacenes:
        id_almacen = x.getid()
        nombre = x.getnombre()
        volumen_total = x.getvolumen_total()
        volumen_dis = x.getvolumen_dis()
        print(id_almacen,' ',nombre,' ', volumen_total,' ',volumen_dis,' ')

def eliminar_item(items,almacenes):        
    listar_items(items,almacenes)
    print('')
    id_encontrado = False
    id_item = int(input('COLOQUE EL ID DEL ITEM QUE DESEA RETIRAR'))
    for x in items:
        if id_item == x.getid():        
            id_encontrado = True
            almacen = x.getalmacen_desig()
            for i in almacenes:
                if almacen == i.getid():
                    items_almacen = i.getitems()
                    for a in items_almacen:
                        if id_item == a.getid():
                            items_almacen.remove(a)
                            a.setitems(items_almacen)
    if id_encontrado == False:
        print('EL ID DEL ITEM COLOCADO NO SE ENCUENTRA')
    else: 
        print('EL ITEM FUE RETIRADO CON EXITO ')


def presentar_menu():
    print('---Almacén Dominicano S.A.---','\n')
    
    desicion_continuar = 'S'
    while desicion_continuar.upper() == 'S':
        print('----PROCESOS---- \n','1-> REGISTRAR ITEM \n', '2-> REGISTRAR ALMACEN \n','3-> RETIRAR ITEM \n', '4-> LISTAR ITEMS \n','5-> LISTAR ALMACENES \n' )
        proceso = int(input('QUE PROCESO DESEA REALIZAR? :'))
        os.system('cls')
        if proceso == 1:
            registrar_item(items)
        elif proceso == 2:
            registrar_almacen(almacenes)
        elif proceso == 3:
            eliminar_item(items,almacenes)
        elif proceso == 4:
            listar_items(items,almacenes)
        elif proceso == 5:
            listar_almacenes(almacenes)
        else:
            print('PROCESO NO ENCONTRADO \n')
            #desicion_continuar = 'S'
        print('')
        desicion_continuar = input('DESEA CONTINUAR CON EL PROGRAMA? S/N :')
        
        if desicion_continuar.upper() == 'N':
            print('HA SELECCIONADO SALIR DEL PROGRAMA')
        
 
presentar_menu()