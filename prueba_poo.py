class Libro:
    #Constructor
    def __init__(self, id, isbn, nombre, cantidad):
        self.id=id
        self.isbn=isbn
        self.nombre=nombre
        self.cantidad=cantidad

    def to_dict(self):
        return {
            "id":self.id,
            "isbn":self.isbn,
            "nombre":self.nombre,
            "cantidad":self.cantidad
        }

    def getid(self):
        return self.id

    def getisbn(self):
        return self.isbn

    def getnombre(self):
        return self.nombre

    def getcantidad(self):
        return self.cantidad

    def setnombre(self, nuevonombre):
        self.nombre=nuevonombre

    def setcantidad(self, nuevacantidad):
        self.cantidad=nuevacantidad

    def setid(self, nuevoid):
        self.id=nuevoid

    def setisbn(self, nuevoisbn):
        self.isbn=nuevoisbn

libros=[]
id_sec=1

def menu(libros):
    

def insertar_libro(isbn, nombre, cantidad, libros):
    global id_sec
    id_sec+=1
    libros.append({'ID': id_sec, 'ISBN':isbn, 'Nombre':nombre, 'Cantidad':cantidad})
    librotemp=Libro(id_sec, isbn, nombre, cantidad)
    #libros.append({'ID': id_sec, 'ISBN':isbn, 'Nombre':nombre, 'Cantidad':cantidad})
    libros.append(librotemp)
    guardar_libros(libros)

def listar_libros(libros):
    librostemp=libros[:]
    #librostemp=libros[:]
    if len(libros)!=0:
        cabecera=list(libros[0].keys())
        imprimirTabla(librostemp, cabecera)
        #for libro in libros:
        #    print("----------------------------") 
        #    print("ID:", libro['ID'])   
        #    print("ISBN:", libro['ISBN'])
        #    print("Nombre:",libro['Nombre'])
        #    print("Cantidad:",libro['Cantidad'])
        #    print("----------------------------") 
        #cabecera=["ID", "ISBN", "Nombre", "Cantidad"]
        #imprimirTabla(librostemp, cabecera)
        for libro in libros:
            print("----------------------------") 
            print("ID:", libro.getid())   
            print("ISBN:", libro.getisbn())
            print("Nombre:",libro.getnombre())
            print("Cantidad:",libro.getcantidad())
            print("----------------------------") 
    else:
        print("No hay libros aún")

def actualizar_libro(id, isbn, nombre, cantidad, libros):
    libro=buscar_libro(id, libros)
    if libro!=None:
        if isbn!="":
            libro['ISBN']=isbn
            libro.setisbn(isbn)
        if nombre!="":
            libro['Nombre']=nombre
            libro.setnombre(nombre)
        if cantidad!="":
            libro['Cantidad']=int(cantidad)
            libro.setcantidad(int(cantidad))
        return 1 #Actualización exitosa
    else:
        return 0 #No existe el libro

def buscar_libro(id, libros):
    for libro in libros:
        if libro['ID']==int(id):
        if libro.getid()==int(id):
            return libro
    return None

@@ -127,13 +170,16 @@ def imprimirTabla(tabla, titulos):
        i+=1

def guardar_libros(libros):
    libros_dict=[libro.to_dict() for libro in libros]
    with open('libros.json','w') as archivo:
        json.dump(libros, archivo, indent=4)
        json.dump(libros_dict, archivo, indent=4)

with open('libros.json','r', encoding='UTF-8') as archivo:
    libros=json.load(archivo)
    libros_dict=json.load(archivo)
    libros=[Libro(libro['id'], libro['isbn'], libro['nombre'], libro['cantidad']) for libro in libros_dict]
    if len(libros)!=0:
        id_sec=libros[len(libros)-1]['ID']  
        id_sec=libros[len(libros)-1].getid()  
    else:
        id_sec=0

menu(libros)