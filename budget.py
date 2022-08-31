from mimetypes import init
from typing import List


class Presupuesto():
    def __init__(self, nombre: str , Fondos: float):
        self.nombre=nombre 
        self.Fondos=Fondos
    
    def aumF(self,cantidad: float):
        self.Fondos:self.Fondos+x
    
    def decF(self,cantidad: float):
        if (self.Fondos>cantidad):
            self.Fondos:self.Fondos-cantidad
        else:
            print("No hay fondos suficientes")

class PresupuestoTotal():
    def __init__(self, list: List):
        self.list=list
        
    def Add(self,Budget: Presupuesto):
        self.list.append(Budget)
        
    def Del(self,Budget: Presupuesto):
        self.list.remove(Budget)
        
    def Transf(self,From: Presupuesto,To: Presupuesto, cantidad: float):
        if (From.Fondos>cantidad):
            From.Fondos:From.Fondos-cantidad
            To.Fondos:To.Fondos+cantidad
        else:
            print("No hay fondos suficientes")
        
    def Porc(self, list: list):
        Total=0
        Porcentaje={}
        for obj in list:
            Total=Total+obj.Fondos