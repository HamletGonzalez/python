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
    
    def setvolumen_dis(self,new_volumen_dis):
        self.volumen_dis = new_volumen_dis
    
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
    
    def setalmacen_desig(self,new_almacen):
            self.almacen_desig = new_almacen

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
            else:   
                items_almacen = x.getitems()
                items_almacen.append({'id_item':id_item,'volumen_item':volumen})
                x.setitems(items_almacen)
                nuevo_volumen = (x.getvolumen_dis() - volumen)
                x.setvolumen_dis(nuevo_volumen)
    if almacen_encontrado == True:
        items.append(item(id_item,descripion,volumen,almacen))
        print('EL ITEM FUE REGISTRADO CON EXITO')
    else:   
        print('EL ITEM NO PUDO SER REGISTRADO ')

def insertar_item(items):
    almacen_encontrado = False
    item_encontrado = False
    listar_items(items,almacenes)
    id_item = int(input('INGRESE EL ID DEL PRODUCTO QUE DESEA INSERTAR'))
    os.system('cls')
    listar_almacenes(almacenes)
    almacen = int(input('INGRESE EL ID DEL ALMACEN A INSERTAR : '))
    for x in items:
        if x.getid() == id_item:
            item_encontrado = True
            volumen = x.getvolumen()
            if x.getalmacen_desig() > 0:
                print('ESTE ITEM YA PERTENECE A UN ALMACEN')
            else:
                for i in almacenes:
                    if i.getid() == almacen:
                        almacen_encontrado = True
                        if (i.getvolumen_dis() - volumen) < (i.getvolumen_total()*0.2):
                            print('EL VOLUMEN DEL ITEM ES MAYOR A LO DISPONIBLE EN ESTE ALMACEN')
                        else:
                            items_almacen = i.getitems()
                            items_almacen.append({'id_item':id_item,'volumen_item':volumen})
                            i.setitems(items_almacen)
                            nuevo_volumen = (i.getvolumen_dis() - volumen)
                            i.setvolumen_dis(nuevo_volumen)
                            x.setalmacen_desig(almacen)
    if item_encontrado == False:
        print('EL ITEM NO PUDO SER ENCONTRADO')
    if almacen_encontrado == True: 
        print('EL ITEM FUE REGISTRADO CON EXITO')
    else:   
        print('HA OCURRIDO UN ERROR CON EL ALMACEN')

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
    largo_id = 1 
    largo_nombre = 1
    largo_volumen_tot = 1
    largo_volumen_dis = 1
    for x in almacenes:
        largo_id_actual = len(str(x.getid()))
        largo_nombre_actual = len(x.getnombre())
        largo_volumen_tot_actual = len(str(x.getvolumen_total()))
        largo_volumen_dis_actual = len(str(x.getvolumen_dis()))
        if largo_id_actual > largo_id:
            largo_id = largo_id_actual
        if largo_nombre_actual > largo_nombre:
            largo_nombre = largo_nombre_actual
        if largo_volumen_tot_actual > largo_volumen_tot:
            largo_volumen_tot = largo_volumen_tot_actual
        if largo_volumen_dis_actual > largo_volumen_dis:
            largo_volumen_dis = largo_volumen_dis_actual
    print('ID','-'*(largo_id+2),'NOMBRE','-'*(largo_nombre),'CAPACIDAD MAXIMA (M3)','-'*(largo_volumen_tot),'CAPACIDAD DISPONIBLE')
    for x in almacenes:
        id_almacen = x.getid()
        nombre = x.getnombre()
        volumen_total = x.getvolumen_total()
        volumen_dis = x.getvolumen_dis()
        print(id_almacen,' '*(largo_id+4-len(str(id_almacen))),nombre,' '*(largo_nombre+6-len(nombre)), volumen_total,' '*(largo_volumen_tot+21-len(str(volumen_total))),volumen_dis,' ')

def eliminar_item(items,almacenes):        
    listar_items(items,almacenes)
    print('')
    id_encontrado = False
    id_item = int(input('COLOQUE EL ID DEL ITEM QUE DESEA RETIRAR :'))
    for x in items:
        if id_item == x.getid():        
            id_encontrado = True
            almacen = x.getalmacen_desig()
            volumen = x.getvolumen()
            for i in almacenes:
                if almacen == i.getid():
                    items_almacen = i.getitems()
                    for a in items_almacen:
                        if id_item == a['id_item']:
                            items_almacen.remove(a)
                            i.setitems(items_almacen)
                            nuevo_volumen = (i.getvolumen_dis() + volumen)
                            i.setvolumen_dis(nuevo_volumen)
                            x.setalmacen_desig(0)
    if id_encontrado == False:
        print('EL ID DEL ITEM COLOCADO NO SE ENCUENTRA')
    elif almacen == 0: 
        print('EL ITEM NO SE ENCUENTRA ACTUALMENTE EN NINGUN ALMACEN')
    else:
        print('EL ITEM FUE RETIRADO CON EXITO')


def presentar_menu():
    print('---Almacén Dominicano S.A.---','\n')
    
    desicion_continuar = 'S'
    while desicion_continuar.upper() == 'S':
        print('----PROCESOS---- \n','1-> REGISTRAR ITEM \n', '2-> REGISTRAR ALMACEN \n','3-> INSERTAR ITEM \n', '4-> RETIRAR ITEMS \n','5-> LISTAR ITEMS \n','6-> LISTAR ALMACENES' )
        proceso = int(input('QUE PROCESO DESEA REALIZAR? :'))
        os.system('cls')
        if proceso == 1:
            registrar_item(items)
        elif proceso == 2:
            registrar_almacen(almacenes)
        elif proceso == 3:
            insertar_item(items)
        elif proceso == 4:
            eliminar_item(items,almacenes)
        elif proceso == 5:
            listar_items(items,almacenes)
        elif proceso == 6:
            listar_almacenes(almacenes)
        else:
            print('PROCESO NO ENCONTRADO \n')
            #desicion_continuar = 'S'
        print('')
        desicion_continuar = input('DESEA CONTINUAR CON EL PROGRAMA? S/N :')
        
        if desicion_continuar.upper() == 'N':
            print('HA SELECCIONADO SALIR DEL PROGRAMA')
        
 
presentar_menu()