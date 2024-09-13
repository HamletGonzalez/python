import json
import os

class empleado:
    def __init__(self,id,nombre,usuario,contrasena) :
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena

    def getid(self):
        return self.id
    
    def getnombre(self):
        return self.nombre
    
    def getusuario(self):
        return self.usuario
    
    def getcontrasena(self):
        return self.contrasena
    
    def to_dict(self):
        return {
            "id":self.id,
            "nombre":self.nombre,
            "usuario":self.usuario,
            "contrasena":self.contrasena
        }
    
class cliente:
    def __init__(self,id,nombre,usuario,contrasena,balance) :
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.balance = balance
                        
    def getid(self):
        return self.id
    
    def getnombre(self):
        return self.nombre
    
    def getusuario(self):
        return self.usuario
    
    def getcontrasena(self):
        return self.contrasena

    def getbalance(self):
        return self.balance
    
    def to_dict(self):
        return {
            "id":self.id,
            "nombre":self.nombre,
            "usuario":self.usuario,
            "contrasena":self.contrasena,
            "balance":self.balance
        }

        
    
empleados = []
clientes = []
def llenar_clientes_empleados():
    clientes.append(cliente(1,'JUAN','JUAN','123456',12000))
    clientes.append(cliente(2,'MARIO','MARIO2','MARIO123',24000))
    empleados.append(empleado(1,'GABRIEL','GABI','GABRIEL001'))

    empleados_dict=[empleado.to_dict() for empleado in empleados]
    with open('empleados.json','w') as archivo:
        json.dump(empleados_dict,archivo,indent=4)
    clientes_dict=[cliente.to_dict() for cliente in clientes]
    with open('clientes.json','w') as archivo2:
        json.dump(clientes_dict,archivo2,indent=4)

llenar_clientes_empleados()
tipo_sesion = 0

def login(tipo_sesion):
    print('BIENVENIDO AL BANCO POPULAR \n\n','INGRESAR COMO: \n','1-> CLIENTE \n','2-> EMPLEADO')
    contrasena_correcta = False
    usuario_encontrado = False
    while tipo_sesion <= 0 or tipo_sesion > 2 :
        tipo_sesion = int(input())
        if tipo_sesion <= 0 or tipo_sesion > 2:
            os.system('cls')
            print('OPCION INVALIDA, FAVOR INTENTAR DE NUEVO \n','INGRESAR COMO: \n','1-> EMPLEADO \n','2-> CLIENTE')
            
        else :
            os.system('cls')
            while contrasena_correcta == False and usuario_encontrado == False:
                print('\n LOGIN:')
                usuario = (input('INGRESE SU USUARIO: '))
                contrasena = (input('INGRESE SU CONTRASENA: '))
                if tipo_sesion == 2:
                    for cliente in clientes:
                        if cliente.getusuario() == usuario.upper():
                            usuario_encontrado = True
                            if cliente.getcontrasena() == contrasena.upper():
                                contrasena_correcta = True
                    if contrasena_correcta == True and usuario_encontrado == True:
                        print('INICIO DE SESION EXITOSO')
                    else :
                        contrasena_correcta = False 
                        usuario_encontrado = False
                        os.system('cls')
                        print('USUARIO O CONTRASENA INCORRECTA, INTENTE NUEVAMENTE')
                if tipo_sesion == 1:
                    for empleado in empleados:
                        if empleado.getusuario() == usuario.upper():
                            usuario_encontrado = True
                            if empleado.getcontrasena() == contrasena.upper():
                                contrasena_correcta = True
                    if contrasena_correcta == True and usuario_encontrado == True:
                        print('\n INICIO DE SESION EXITOSO')
                    else :
                        contrasena_correcta = False 
                        usuario_encontrado = False
                        os.system('cls')
                        print('USUARIO O CONTRASENA INCORRECTA, INTENTE NUEVAMENTE')

login()       

def imprimir_menu(tipo_sesion):
    os.system('cls')
    proceso = 0
    desicion = 'S'
    print('QUE PROCESO DESEA REALIZAR: \n')
    if tipo_sesion == 1:
        while desicion == 'S':
            while proceso <= 0 or proceso > 4:
                print('1-> REGISTRAR UN CLIENTE: \n','2-> LISTAR CLIENTES\n','3-> VER TRANSFERENCIAS\n','4-> CAMBIAR ESTATUS DE UN CLIENTE\n')
                proceso = int(input())
                if proceso == 1:
                    print('')
                elif proceso == 2:
                    print('')
                elif proceso == 3:
                    print('')
                elif proceso == 4:    
                    print('')
                else:
                    print('PROCESO INVALIDO, INTENTE NUEVAMENTE ')
            int(input('DESEA CONTINUAR? S/N'))
        if tipo_sesion == 2:
            while proceso <= 0 or proceso > 4:
                print('1-> REGISTRAR UN CLIENTE: \n','2-> LISTAR CLIENTES\n','3-> VER TRANSFERENCIAS\n','4-> CAMBIAR ESTATUS DE UN CLIENTE')        