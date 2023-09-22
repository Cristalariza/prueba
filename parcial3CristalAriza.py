#programa que llena, ordena, muestra, busca, y elimina elementos 
import random
datos=[]

def menu():
    print("-----MENU OPCIONES PARCIAL-----")
    print("1 llenado\n2 ordenamientos\n3 Mostrar todos los elementos\n4 Buscar elemento\n5 Eliminar elementos\n6 salir")
    opcion= input("Ingrese una opción a elegir: ")
    return opcion

def llenado():
    z=int(input("Digite la cantidad de elementos: "))
    for i in range(0,z):
        x=(random.randint(1, 500))
        datos.append(x)

def mostrar():
    for i in datos:
        print(i)

def burbuja(datosBurbuja):
    print("\nOrdenando por Burbuja....")
    for i in range(1,len(datosBurbuja)):
        for j in range(0,len(datosBurbuja)-i):
            if(datosBurbuja[j+1] < datosBurbuja[j]):
                aux=datosBurbuja[j];
                datosBurbuja[j]=datosBurbuja[j+1];
                datosBurbuja[j+1]=aux;
    datos=[]
    datos = datosBurbuja
    print("Ordenado")

def insercion(datosInsercion):
    print("\nOrdenando por Insercion ....")
    for i in range(len(datosInsercion)):
        for j in range(i,0,-1):
            if(datosInsercion[j-1] > datosInsercion[j]):
                aux=datosInsercion[j];
                datosInsercion[j]=datosInsercion[j-1];
                datosInsercion[j-1]=aux;
    datos=[]
    datos = datosInsercion
    print("Ordenado")

def shell(lista):
    print("\nOrdenando por Shell....")
    mitad = len(lista) // 2
    while mitad > 0:
        for p in range(mitad):
            reducir_busqueda(lista , p, mitad)
        mitad = mitad // 2
    datos = []
    datos = lista
    print("Ordenado")

def reducir_busqueda(lista, inicio , salto):
    for i in range(inicio + salto, len(lista), salto):
        valor = lista[i]
        posicion = i 
        while posicion >= salto and lista[posicion - salto] > valor:
            lista[posicion] = lista[posicion - salto]
            posicion = posicion - salto
        lista[posicion] = valor

def ordenamiento():
    print("-----MENU ORDENAMIENTO-----")
    print("1 Burbuja\n2 Insercición\n3 Shell")
    opcion= input("Ingrese una opción a elegir: ")
    if opcion == "1":
        burbuja(datos)
    elif opcion == "2":
        insercion(datos)
    elif opcion == "3":
        shell(datos)
    else:
        print("Opcion incorrecta")

def buscar():
    numero = int(input("Ingrese el numero a buscar: "))
    encontro = False
    for i in datos:
        if numero == i:
            encontro = True
    if encontro == True:
        print("el "+ str(numero) + " si existe")
    else:
        print("No existe el elemento")        

def eliminar():
    numero = int(input("Ingrese el numero que quiere eliminar: "))
    elimino = False
    for i in datos:
        if(i == numero):
            datos.remove(i)
            elimino = True
            print("Elemento eliminado...")

    if elimino == False:
        print("No fue encontrado...")

        

while True:
    op= menu()
    if op=="1":
        llenado()
    elif op == "2":
        ordenamiento()
    elif op == "3":
        mostrar()
    elif op == "4":
        buscar()
    elif op == "5":
        eliminar()
    elif op == "6":
        exit()
    else:
        print("Operación no valida")