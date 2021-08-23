class Lista:
    def __init__(self,tamanio=3):
        self.lista = []
        self.longitud = 0
        self.size = tamanio
        
    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud+= 1
            return True
        else:
            return False
        
            
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]
        
    def obtenerEliminado(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else: 
           eliminado = self.lista[pos]
            self.lista = self.lista[:pos] + self.lista[pos+1:]
            print( "La lista queda: {} y el elemento eliminado es {}".format(self.lista,eliminado))
            # listaAux = []
            # for ind in range(pos):
            #     listaAux += [self.lista[ind]]
            # for indice in range(pos+1,self.longitud):
            #     listaAux += [self.lista[indice]] 
            # self.longitud -=1
            # self.lista = listaAux
            # return [self.lista,eliminado] 
    
    #busca un valor en la lista y retorna la posicion de ese valor en la lista
    def buscar(self,dato):
        if dato in self.lista:
            self.res = self.lista.index(dato)
            print("la posicion del dato es ",self.res)
            return True
        else:
            return False
    
    #busca un dato con el metodo buscar y si no lo encuentra lo insertas    
    def insertar(self,dato):
        if self.buscar(dato) == False:
            self.size += 1
            self.append(dato)
        return self.lista
    
    #busca el dato con el metodo buscar y si lo encuentra lo elimina de la lista
    def eliminar(self,dato,):
        if self.buscar(dato) == True:
            self.obtenerEliminando(self.res)
        else:
            False
     
    def mostrar(self):
        print("{:3} {}".format("Lista","Posicion"))
        for pos, ele in enumerate(self.lista):
            print("[{:6}] {:3}".format(ele,pos))
            
               
# lista1 = Lista()
# lista1.append("Jairo")
# lista1.append("21")
# lista1.append(True)
# # print(lista1.obtener(1))
# lista1.eliminar("Jairo")
# print(lista1.buscar(21))
# print(lista1.insertar(22))
#lista1.append("Milagro")
# lista1.mostrar()
# posicion = int(input("Ingrese posicion para obtener el valor del elemento "))
# resp =lista1.obtenerEliminado(posicion)
# if resp == None:
#     print("Posicion no valida, verifique la lista ")
# else:
#     print("El elemento de la posicion:{} es:{}".format(posicion,resp))
        
        
              
