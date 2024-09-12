import json

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
    

