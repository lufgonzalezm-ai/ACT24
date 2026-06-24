
from Funciones import *
from os import system

while True:
    try:
        system("pause")
        system("cls")
        print(f"""
===== MENU DE GESTION GREMIAL =====
1. Registrar personajes
2. Buscar Personaje por Nombre
3. Elminar Personaje
4. Subir de nivel a un Personaje
5. Calcular Estadisticas Generales
6. Mostrar lista de Miembros
7. Salir del Sistema
===================================""")
        opcion = int(input("Seleccione : "))

        match opcion:
            case 1:
                nombre = input("Ingrese nombre : ").title()
                clase = input("Ingrese Clase : ").title()
                nivel = int(input("Ingrese Nivel : "))
                agregar(nombre,clase,nivel)
            case 2:
                nombre = input("Ingrese nombre : ").title()
                mostrar(nombre)
            case 3: 
                nombre = input("Ingrese nombre que desee eliminar : ").title()
                eliminar(nombre)
            case 4: 
                nombre = input("Ingrese nombre para subir nivel : ")
                SubirNivel()
            case 5:pass
            case 6: listar()
            case 7: break
            case _: print("Error")
    except Exception as e:
        print(f"Error {e}")
