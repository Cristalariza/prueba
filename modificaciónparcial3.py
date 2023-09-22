
import random
datos_vector=[]

def menu1():
    while True:
        print("-----MENU OPCIONES PARCIAL-----")
        print("1 llenado\n2 ordenamientos\n3 Mostrar todos los elementos\n4 Buscar elemento\n5 Eliminar elementos\n6 Reporte\n7 Salir\nMenú hecho por Cristal Ariza")
        opcion= input("Ingrese una opción a elegir: ")
        return opcion

def llenado():
    z=int(input("Digite la cantidad de elementos: "))
    for i in range(0,z):
        x=(random.randint(1, 500))
        datos_vector.append(x)

def ordenamientos():
    op = menu2()
    if op=="1": 
        burbuja(datos_vector)  
    elif op=="2":
        inserción(datos_vector)
    elif op=="3":
        shell(datos_vector)
    elif op=="4":
        print("volviendo... ")
    else:
        print("opción incorrecta, no valida")

def burbuja(datosBurbuja):
    print("\nOrdenando por Burbuja....")
    for i in range(1,len(datosBurbuja)):
        for j in range(0,len(datosBurbuja)-i):
            if(datosBurbuja[j+1] < datosBurbuja[j]):
                aux=datosBurbuja[j]
                datosBurbuja[j]=datosBurbuja[j+1]
                datosBurbuja[j+1]=aux
    datos_vector=[]
    datos_vector = datosBurbuja
    print("Ordenado")


def inserción(datosInsercion):
    print("\nOrdenando por Insercion ....")
    for i in range(len(datosInsercion)):
        for j in range(i,0,-1):
            if(datosInsercion[j-1] > datosInsercion[j]):
                aux=datosInsercion[j];
                datosInsercion[j]=datosInsercion[j-1];
                datosInsercion[j-1]=aux;
    datos_vector=[]
    datos_vector = datosInsercion
    print("Ordenado")


def shell(lista):
    print("\nOrdenando por Shell....")
    mitad = len(lista) // 2
    while mitad > 0:
        for p in range(mitad):
            reducir_busqueda(lista , p, mitad)
        mitad = mitad // 2
    datos_vector = []
    datos_vector = lista
    print("Ordenado")

def reducir_busqueda(lista, inicio , salto):
    for i in range(inicio + salto, len(lista), salto):
        valor = lista[i]
        posicion = i 
        while posicion >= salto and lista[posicion - salto] > valor:
            lista[posicion] = lista[posicion - salto]
            posicion = posicion - salto
        lista[posicion] = valor


def mostrar_elementos():
    if datos_vector == []:
        print("No hay nada en la lista")
    else:
        for i in datos_vector:
            print(i)
    

def buscar_elemento():
    numero = int(input("Ingrese el numero a buscar: "))
    encontro = False
    contador = 0
    for i in datos_vector:
        if numero == i:
            contador = contador + 1
            encontro = True
    if encontro == True:
        print("el "+ str(numero) + " si existe")
        print("se encontro: " + str(contador) + " veces")
    else:
        print("No existe el elemento")  

def eliminar_elemento():
    numero = int(input("Ingrese el numero que quiere eliminar: "))
    elimino = False
    for i in datos_vector:
        if(i == numero and elimino == False):
            datos_vector.remove(i)
            elimino = True
            print("Elemento eliminado...")

    if elimino == False:
        print("No fue encontrado...")

def reporte():
    mayor_elemento = max(datos_vector)
    total_datos = sum(datos_vector)
    cantidad_datos = len(datos_vector)
    promedio_datos = total_datos/cantidad_datos
    contador = 0
    for num in datos_vector:
        if num % 2 == 0:
            contador = contador + 1

    print('El mayor elemento es:', mayor_elemento)
    print("el promedio es: ", promedio_datos)
    print("hay", contador, "numeros pares")

def menu2():
    print("-----MENU ORDENAMIENTO-----")
    print("1 burbuja\n2 inserción\n3 shell\n4 volver\n")
    opcion= input("Ingrese una opción a elegir: ")
    return opcion

while True:
    op= menu1()
    if op=="1":
        llenado()
    elif op == "2":
        ordenamientos()
    elif op == "3":
        mostrar_elementos()
    elif op == "4":
        buscar_elemento()
    elif op == "5":
        eliminar_elemento()
    elif op == "6":
        reporte()
    elif op == "7":
        exit()
    else:
        print("Operación no valida")
