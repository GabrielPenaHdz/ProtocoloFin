from ntpath import join
import os
from timeit import repeat
import itertools

def menu():
    print (". - . - . - . - . - . - . - . - . - . - . - Menu Principal . - . - . - . - . - . - . - . - . - . - . -")
    print("")
    print("1.- Crear protocolo")
    print("2.- Agregar instruccion")
    print("3.- Consultar el protocolo completo")
    print("4.- Eliminar una instruccion")
    print("5.- Salir")
    print("Hay un maximo de 10 pasos para el protocolo")
    print(". - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - . - ")

protocolo = []
inst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    menu()
    opc = int(input("Escoja una opcion: "))
    if opc == 1:
        print("Se ha creado el protocolo ")
        print(". - . - . - . - . - . - . - . - . - ")
        print("")
    elif opc == 2:
        a = input("Escriba la instruccion: ")
        protocolo.append(a)
        more = input ("Deseas escribir otra instrucciOn? s/n: ")
        if more == "s":
            pasos = int(input("Cuantas instrucciones quieres incluir al protocolo?: "))
            for x in itertools.repeat(None, pasos):
                a = input("Escriba la nueva instruccion: ")
                protocolo.append(a)
        elif more == "n":
            print("")
            menu() 
        else: 
            print("Opcion indefinida")
            print("")
    elif opc == 4:
        elim = int(input("Que instruccion quieres eliminar?: (escribir el nmero dado por la opcion 3) "))
        protocolo.pop(elim)
        print ("Se ha eliminado la instruccion",elim)
        print("")
    elif opc == 3:
        union = list(zip(inst, protocolo))
        for i in union:
            print(i)
    elif opc == 5:
        print("Hasta luego")
        break
    else:
        print("Escoja una opcion valida")