class Cola:
    def __init__(self,tamanio=3):
        self.lista = []
        self.size = tamanio
        self.top = 0

    def insertar(self,dato):
        if self.top < self.size:
            self.lista += [dato]
            self.top += 1
            return True
        else:
            return False

    def quitar(self):
        if self.empty():
            return None
        else:
            pri = self.lista.pop(0)
            self.top -= 1
            return pri

    def empty(self):
         if self.top == 0:
            return True
         else:
            return False

    def mostrar(self):
        for top in range(self.top):
            print("[{}]".format(self.lista[top]))

    def longitud(self):
        return self.top
#
# cola1= Cola()
# cola1.insertar(1)
# cola1.insertar(2)
# cola1.insertar(3)
# #print(cola1.quitar())
        
    
