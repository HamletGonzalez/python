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
    def __init__(self,id,nombre,usuario,contrasena,balance,estado,movimientos) :
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena
        self.balance = balance
        self.estado = estado
        self.movimientos = movimientos
                            
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
    
    def getestado(self):
        return self.estado
    
    def getmovimientos(self):
        return self.movimientos
    
    def to_dict(self):
        return {
            "id":self.id,
            "nombre":self.nombre,
            "usuario":self.usuario,
            "contrasena":self.contrasena,
            "balance":self.balance,
            "estado":self.estado,
            "movimientos":self.movimientos
        }
    
    def setbalance(self,new_balance):
        self.balance = new_balance

    def setmovimientos(self,nuevo_movimiento):
        self.movimientos = nuevo_movimiento
        
    

        
    
empleados = []
clientes = []
movimientos = []
def llenar_clientes_empleados():
    """    clientes.append(cliente(1,'JUAN','JUAN','123456',12000,'A',[]))
    clientes.append(cliente(2,'MARIO','MARIO2','MARIO123',24000,'I',[]))
    empleados.append(empleado(1,'GABRIEL','GABI','GABRIEL001'))

    empleados_dict=[empleado.to_dict() for empleado in empleados]
    with open('empleados.json','w') as archivo:
        json.dump(empleados_dict,archivo,indent=4)
    clientes_dict=[cliente.to_dict() for cliente in clientes]
    with open('clientes.json','w') as archivo2:
        json.dump(clientes_dict,archivo2,indent=4)"""

def cargar_datos():
    global empleados
    global clientes
    global movimientos
    with open ('empleados.json','r') as archivo:
        datos = json.load(archivo)
        #datos_dict = json.load(archivo)
        datos=[empleado(Empleado['id'], Empleado['nombre'], Empleado['usuario'], Empleado['contrasena']) for Empleado in datos]
        empleados = datos
    
    with open ('clientes.json','r') as archivo2:
        datos2 = json.load(archivo2)
        #datos2_dict = json.load(archivo2)
        datos2=[cliente(Cliente['id'], Cliente['nombre'], Cliente['usuario'], Cliente['contrasena'],Cliente['balance'],Cliente['estado'],Cliente['movimientos']) for Cliente in datos2]
        clientes = datos2

    with open ('movimientos.json','r') as archivo3:
        datos3 = json.load(archivo3)
        #datos2_dict = json.load(archivo2)
        #datos3=[(movimientos['numero'], movimientos['usuario'], movimientos['monto'], movimientos['beneficiario']) for movimientos in datos3]
        movimientos = datos3


        

cargar_datos()
llenar_clientes_empleados()
tipo_sesion = 0
codigo_usuario = 0

def login():
    global codigo_usuario
    global tipo_sesion
    print('BIENVENIDO AL BANCO POPULAR \n\n','INGRESAR COMO: \n','1-> EMPLEADO \n','2-> CLIENTE')
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
                                codigo_usuario = cliente.getid()
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
                                codigo_usuario = empleado.getid()
                    if contrasena_correcta == True and usuario_encontrado == True:
                        print('\n INICIO DE SESION EXITOSO')
                        return codigo_usuario, tipo_sesion
                        #return tipo_sesion
                    else :
                        contrasena_correcta = False 
                        usuario_encontrado = False
                        os.system('cls')
                        print('USUARIO O CONTRASENA INCORRECTA, INTENTE NUEVAMENTE')

login()

def consultar_balance():
    print('HA ELEGIDO LA OPCION DE CONSULTAR BALANCE')       
    for cliente in clientes:
        if cliente.getid() == codigo_usuario:
            print('SU BALANCE ACTUAL ES DE: ',cliente.getbalance(),'RD$')

def realizar_transferencia():
    cuenta_encontrada = False
    print('HA ELEGIDO LA OPCION DE REALIZAR TRANSFERENCIA\n A QUE CUENTA DESEA REALIZAR LA TRANSFERENCIA? ')
    cuenta_transferencia = int(input())
    if cuenta_encontrada == codigo_usuario:
        print('LA CUENTA NO PUEDE SER LA MISMA DE ESTA SESION')
    else:
        for cliente in clientes:
            if cliente.getid() == cuenta_transferencia:
                cuenta_encontrada = True
                mensaje = ''
                print('LA CUENTA INGRESADA SE ENCUENTRA AL NOMBRE DE ',cliente.getnombre(),'\nQUE MONTO DESEA TRANSFERIR? ',)
                monto_transferencia = int(input())
                for usuario in clientes:
                    if usuario.getid() == codigo_usuario:
                        if monto_transferencia > usuario.getbalance() or monto_transferencia <= 0:
                            print('error: EL MONTO INGRESADO NO ES VALIDO')
                            cuenta_encontrada = False
                        else:
                            nuevo_balance_usuario = usuario.getbalance() - monto_transferencia
                            usuario.setbalance(nuevo_balance_usuario)
                            nuevo_balance_receptor = cliente.getbalance() + monto_transferencia 
                            cliente.setbalance(nuevo_balance_receptor)
                            guardar_transferencia(codigo_usuario,monto_transferencia,cliente.getid())
                            print('TRANSFERENCIA EXITOSA')
            else:
                mensaje = 'EL NUMERO DE CUENTA INGRESADO NO SE ENCONTRO'                
        if cuenta_encontrada == False:
            print('FALLO AL REALIZAR LA TRANSFERENCIA, FAVOR REVISAR',mensaje)
                
def guardar_transferencia(codigo_usuario,monto,beneficiario):
    numero = len(movimientos) + 1
    
    nuevo_movimiento = {'numero':numero,'usuario':codigo_usuario,'monto':monto,'beneficiario':beneficiario}
    movimientos.append(nuevo_movimiento)
    for usuario in clientes:
        if usuario.getid() == codigo_usuario:
            movimientos_ant = usuario.getmovimientos()
            movimientos_ant.append(nuevo_movimiento)
            usuario.setmovimientos(movimientos_ant)
            movimientos_dict=[usuario.getmovimientos() for movimiento in movimientos]
            with open('movimientos.json','w') as archivo:
                json.dump(movimientos_dict,archivo,indent=4)    

def abonar_cuenta():
    print('HA SELECCIONADO  LA OPCION PARA ABONAR SU CUENTA\nQUE MONTO DESEA ABONAR?')
    monto_abonar = int(input())
    if monto_abonar <= 0:
        print('EL MONTO NO PUEDE SER MENOR A CERO')
    else:
        print('\nINGRESE SU CONTRASENA PARA CONFIRMAR SU IDENTIDAD')
        contrasena = input()
        for usuario in clientes:
            if codigo_usuario == usuario.getid():
                if contrasena.upper() == usuario.getcontrasena():
                    balance_nuevo = usuario.getbalance() + monto_abonar 
                    usuario.setbalance(balance_nuevo)
                    print('PROCESO COMPLETADO CON EXITO\nSU NUEVO BALANCE ES DE: ',usuario.getbalance())
                else:
                    print('LA CONFIRMACION DE IDENTIDAD NO PUDO SER COMPLEATADA CON EXITO')

def consultar_movimientos():
    print('')

def registrar_clientes():
    print('HA SELECCIONADO LA OPCION DE REGISTAR CLIENTE\n')
    id = len(clientes) + 1
    nombre = input('INGRESE EL NOMBRE COMPLETO DEL CLIENTE\n')
    usuario = input('INGRESE EL USUARIO CON EL CUAL INICIARA SESION\n')
    contrasena = input('INGRESE LA CONSTRASENA CON LA CUAL INICIARA SESION\n')
    balance = int(input('CUAL SERA EL BALANCE INICIAL DEL CLIENTE?\n'))
    if balance <= 0:
        print('EL BALANCE INICIAL NO PUEDE SER MENOR A CERO')
    else:
        clientes.append(cliente(id,nombre.upper(),usuario,contrasena,balance,'A',[]))
        print('CLIENTE REGISTRADO CON EXITO')

    
def imprimir_menu():
    os.system('cls')
    proceso = 0
    desicion = 'S'
    print('QUE PROCESO DESEA REALIZAR: \n')
    if tipo_sesion == 1:
        while desicion.upper() == 'S':
            while proceso <= 0 or proceso > 4:
                print('1-> REGISTRAR UN CLIENTE \n','2-> LISTAR CLIENTES\n','3-> VER MOVIMIENTOS\n','4-> CAMBIAR ESTATUS DE UN CLIENTE\n')
                proceso = int(input())
                if proceso == 1:
                    print('')
                    registrar_clientes()
                elif proceso == 2:
                    print('')
                elif proceso == 3:
                    print('')
                elif proceso == 4:    
                    print('')
                else:
                    print('PROCESO INVALIDO, INTENTE NUEVAMENTE ')
            desicion = input('DESEA CONTINUAR? S/N   ')
    if tipo_sesion == 2:
        while proceso <= 0 or proceso > 4:
            print('1-> CONSULTAR BALANCE \n','2-> REALIZAR TRANSFERENCIAS\n','3-> ABONAR CUENTA\n','4-> VER MOVIMIENTOS')        
            proceso = int(input())
            if proceso == 1:
                print('')
                consultar_balance()
            elif proceso == 2:
                print('')
                realizar_transferencia()
            elif proceso == 3:
                print('')
                abonar_cuenta()
            elif proceso == 4:    
                print('')
            else:
                print('PROCESO INVALIDO, INTENTE NUEVAMENTE ')
        input('DESEA CONTINUAR? S/N  ')
    print('HA SALIDO DEL SISTEMA')
    empleados_dict=[empleado.to_dict() for empleado in empleados]
    with open('empleados.json','w') as archivo:
        json.dump(empleados_dict,archivo,indent=4)
    clientes_dict=[cliente.to_dict() for cliente in clientes]
    with open('clientes.json','w') as archivo2:
        json.dump(clientes_dict,archivo2,indent=4)

imprimir_menu()