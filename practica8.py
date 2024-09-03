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

class item:
    def __init__(self,id,descripcion,volumen,almacen_desig) :
        self.id = id
        self.descripcion = descripcion
        self.volumen_total = volumen
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
    items.append(item(5,'NEUMATICOS',80,0))
    
def llenar_almacenes(almacenes):
    almacenes.append(almacen(1,'BODEGA DE MATERIALES',250,))
    almacenes.append(item(2,'MESA',50,2))
    items.append(item(3,'SILLAS',60,2))
    items.append(item(4,'TELAS',20,0))
    items.append(item(5,'NEUMATICOS',80,0))
    

llenar_items(items,almacenes)

def registrar_item(items):
    id_item = len(items) + 1
    descripion = input('INGRESE LA DESCRIPCION DEL ITEM A REGISTRAR : ')
    volumen = int(input('INGRESE EL VOLUMEN (cm3) DEL ARTICULO : '))
    almacen = int(input('INGRESE EL ID DEL ALMACEN DEL ARTICULO : '))
    for x in almacenes:
        if x.getid() == almacen:
            
    
    
