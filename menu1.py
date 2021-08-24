import os
from listas import Lista
from pila import Pila
from colas import Cola

class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija opcion [1....{}]: ".format(len(self.opciones)))      
        return opc
opc = ""
while opc != "4":
    os.system("cls")
    men = Menu("Menú Estructuras",["1) Listas","2) Colas","3) Pilas","4) Salir"])
    opc = men.menu()
    tam=int(input("Ingrese tamaño: "))
    pila1 = Pila(tam)
    lista1 = Lista(tam)
    cola1 = Cola(tam)
    if opc == "1":
        opc1 = ""
        while opc1 != "8":
            os.system("cls") 
            men1 = Menu("Menú Listas",["1) Append","2) Obtener","3) ObtenerEliminasdo","4) Buscar","5) Insertar","6) Eliminar","7) Mostrar","8) Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                for i in range(tam):
                    dato = int(input("Ingrese el numero que desea ingresar a la lista: "))
                    lista1.append(dato)
                    print("Dato ingresado")
                input("Presione una tecla para continuar")
            elif opc1 == "2":
                os.system("cls")
                print("Obtener un dato de una lista")
                pos =int(input("Ingrese posicion del dato: "))
                print(lista1.obtener(pos))
                input("Presione una tecla para continuar")
            elif opc1== "3":
                os.system("cls")
                print("Obtener el valor eliminado junto a la lista")
                pos = int(input("Ingrese posicion del dato: "))
                lista1.obtenerEliminado(pos)
                input("Presione una tecla para continuar")
            elif opc1== "4":
                os.system("cls")
                print("Buscar elemento en la lista y retornar la posicion")
                pos = int(input("Ingrese el dato a buscar: "))
                print(lista1.buscar(pos))
                input("Presione una tecla para continuar")
            elif opc1 == "5":
                os.system("cls")
                print("Insertar dato en la lista desconocido de la lista")
                dato = int(input("Ingres dato a buscar para insertarlo: "))
                print(lista1.insertar(dato))
                input("Presione una tecla para continuar")
            elif opc1 == "6":
                os.system("cls")
                print("Eliminar el dato de la lista si llega ha exitir en la lista")
                dato = int(input("Ingrese el dato a buscar para eliminarlo: "))
                print(lista1.eliminar(dato))
                input("Presione una tecla para continuar")
            elif opc1 == "7":
                os.system("cls")
                print("Mostrar los datos de la lista")
                lista1.mostrar()
                input("Presione una tecla para continuar")
            elif opc1 == "8":
                print("De vuelta al Menu Principal")
                input("Presione una tecla para continuar")
            else:
                print("OPCION NO VALIDA")
                input("Presione una tecla para continuar")
    elif opc == "2":
        opc2 = ""
        while opc2 != "6":
            os.system("cls")
            men2 = Menu("Menu Cola", ["1)Insertar", "2)Quitar", "3)Mostrar", "4)Longitud", "5)Empty", "6)Salir"])
            opc2 = men2.menu()
            if opc2 == "1":
                os.system("cls")
                print("Ingrese un numero a la Cola")
                for i in range(tam):
                    dato = int(input("Ingrese el numero que se desea ingresar a la cola: "))
                    cola1.insertar(dato)
                    print("Dato ingresado")
                input("Presione una tecla para continuar")
            elif opc2 == "2":
                os.system("cls")
                print("Quitar el primer valor de la Cola")
                ele1 = int(input("Cuantos elemento desea quitar de la cola: "))
                if ele1 <= tam:
                    for i in range(ele1):
                        print("El elemento eliminado es: {}".format(cola1.quitar()))
                    input("Presione una tecla para continuar")
                else:
                    print("Error, el numero es mayor al tamaño de la cola")
                    input("Presione una tecla para continuar")
            elif opc2 == "3":
                os.system("cls")
                print("Mostrar los valores de la Cola")
                cola1.mostrar()
                input("Presione una tecla para continuar")
            elif opc2 == "4":
                os.system("cls")
                print("Mostrar la longitud de la Cola")
                print("La longitud de cola es: {}".format(cola1.longitud()))
                input("Presione una tecla para continuar")
            elif opc2 == "5":
                os.system("cls")
                print("Verifique si la Cola está vacia ")
                print("{}".format(cola1.empty()))
                input("Presione una tecla para continuar")
            elif opc2 == "6":
                print("De vuelta al Menu Principal")
                input("Presione una tecla para continuar")
            else:
                print("Opción no valida")
                input("Presione una tecla para continuar")
                
    elif opc == "3":
        opc3 =""
        while opc3 != "6":
            os.system("cls")
            men1 = Menu("Menu Pila",["1)Push","2)Pop","3)Show","4)Longitud","5)Empty","6)Salir"])
            opc1 = men1.menu()
            if opc1 =="1":
                os.system("cls")
                print("Ingreso de un numero a la Pila")
                for i in range(tam):
                    dato = int(input("Ingrese el numero que desea ingresar a la pila: "))
                    print("Dato no válido, por favor ingrese un número")
                    pila1.push(dato)
                    print("Dato ingresado")
                input("Presione una tecla para continuar")
            elif opc1 == "2":
                os.system("cls")
                print("Quitar el ultimo digito de la Pila")
                while True:
                    try:
                        x = int(input("Cuantos elemento se desea quitar de la Pila: "))
                        break
                    except ValueError:
                        print("Dato no válido, por favor ingrese un número")
                if x <= tam:
                    for i in range(x):
                        print("El elemento quitado es: {}".format(pila1.pop()))
                    input("Presione una tecla para continuar")
                else:
                    print("Error numero mayor tamaño de la pila o no exite una pila")
                    input("Presione una tecla para continuar")
            elif opc1 =="3":
                os.system("cls")
                print("Mostrar los valores de la Pila")
                pila1.show()
                input("Presione una tecla para continuar")
            elif opc1 == "4":
                os.system("cls")
                print("Mostrar la longitud de la Pila")
                print("La longitud de la pila es: {}".format(pila1.longitud()))
                input("Presione una tecla para continuar")
            elif opc1 =="5":
                os.system("cls")
                print("Verificar si la Pila está vacia")
                print("False para pila llena y True para pila vacia")
                print("{}".format(pila1.empty()))
                input("Presione una tecla para continuar")
            elif opc1 =="6":
                print("De vuelta al Menu Principal")
                input("Presione una tecla para continuar")
            else:
                print("Opción no valida")
                input("Presione una tecla para continuar") 
            
    elif opc == "4":
        print("GRACIAS POR USAR EL SISTEMA") 
    else: 
        print("OPCION NO VALIDA") 
        print("Lo esperemas en otra ocasion")           
        
        