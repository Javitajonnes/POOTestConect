from Database import *
from os import system

db=Database()
while True:
    elige=input('\nElija una opcion:\n\
    \tMostrar un repuesto(u)\n\
    \tMostrar todos los repuestos(t)\n\
    \tInsertar()\n\
    \tEliminar (e)\n\
    \tFin (f)\n\
    \t=>').lower()
    if elige=='u':
        codAbuscar=input('Ingrese codigo a buscar=')
        db.select_uno(codAbuscar)
    elif elige=='t':
        db.select_todos()
    elif elige=='i':
        db.insertar()
    elif elige=='e':
        db.eliminar()
    elif elige=='f':
        print('Fin')
        db.cerrarBD()
        break
    else:
        print('Error de opcion')

    input('Pulse enter para continuar...')
    system('cls')        