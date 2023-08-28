from televisores.marca import Marca

class TV:

    _numTV = 0
   
    def __init__(self, marca, estado):
        
        self._marca = marca 
        self._canal = 1 
        self._precio = 500 
        self._estado = estado
        self._volumen = 1 
        self._control = None
        TV._numTV += 1

    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca

    def getCanal(self):
        return self._canal
    
    def setCanal(self, num):
        
        if self._estado == True and num >= 1 and num <= 120:
          self._canal = num
        
    def getPrecio(self):
        return self._precio
    
    def setPrecio(self, num):
        self._precio = num

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self, num):

        if self._estado == True and num >= 0 and num <= 7:
          self._volumen = num
        

    def getControl(self):
        return self._control
    
    def setControl(self, control):
        self._control = control

    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    @classmethod
    def setNumTV(cls, num):
        cls._numTV = num

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._estado == True and self._canal < 120 and self._canal >= 1 :
            self._canal += 1

    def canalDown(self):
        if self._estado == True and self._canal > 1 and self._canal <= 120:
            self._canal -= 1

    def volumenUp(self):
        if self._estado == True and self._volumen < 7 and self._volumen >= 0:
            self._volumen += 1

    def volumenDown(self):
        if self._estado == True and self._volumen > 0 and self._volumen <= 7:
            self._volumen -= 1