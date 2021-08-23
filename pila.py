class Pila:
    def __init__(self,tamanio=1):
        self.lista=[]
        self.size=tamanio
        self.top=0
        
    def push(self,dato): #2   
        if self.top < self.size:
            self.lista = self.lista + [dato]
            self.top += 1
        else:
            print("La lista esta llena")
            
    def pop(self): #3
        if self.empty():
            return None
        else:
            top = self.lista[-1]
            self.lista = self.lista[:-1]
            self.top -= 1
            return top
        
    def show(self): #4
        for top in range(self.top-1,-1,-1):
            print("[{}]".format(self.lista[top]))
       
    def longitud(self): 
        return self.top 
    
    def empty(self): #1
        if self.top == 0:
            return True
        else:
            return False
    
    
    
pila1 = Pila(3)
pila1.push(8)
pila1.push(10)
pila1.push(12)
pila1.show()
print(pila1.longitud())
#pila1.push(4)

# dato = pila1.pop()
# if dato: print("el dato eliminado es: {}".format(dato))
# else: print("La lista esta vacia")
# dato = pila1.pop()
# if dato: print("el dato eliminado es: {}".format(dato))
# else: print("La lista esta vacia")
# dato = pila1.pop()
# if dato: print("el dato eliminado es: {}".format(dato))
# else: print("La lista esta vacia")
# dato = pila1.pop()
# if dato: print("el dato eliminado es: {}".format(dato))
# else: print("La lista esta vacia")
#pila1.show()


