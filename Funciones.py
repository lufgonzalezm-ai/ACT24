#Coleccion para almacenar temporalmente los personajes

personajes = []

def buscar(nombre):
    for i in range(len(personajes)):
        if personajes[i]["nombre"] == nombre:
            return i #Retornamos la posición donde está (Si es que está)
    return -1 #Si el personaje no se encuentra es -1

def agregar(nombre,clase,nivel):
    #Validar los datos
    if len(nombre.strip())==0 or len(nombre.strip())>20:
        print("Nombre no válido")
        return
    elif buscar(nombre)>=0:
        print("Nombre ya existe")
        return
    elif clase not in ("Guerrero","Mago","Pícaro"):
        print("Clase no válida, debe ser Guerrero, Mago o Pícaro")
        return
    elif nivel<=0 or nivel>50:
        print("El nivel debe estar entre 1 y 50")
        return
    #Registrar personaje en la lista
    rango = "Recluta"
    if nivel>=30: rango = "Elite"
    pj = {"nombre":nombre,"clase":clase,"nivel":nivel,"rango":rango}
    personajes.append(pj)
    print("Personaje Registrado")

def mostrar (nombre):
    posicion = buscar(nombre)
    if posicion >= 0:
        print(f"Persona encontrada : ) {personajes[posicion]}")
    else:
        print("Nombre no existe")

def listar():
    if len(personajes)>0:
        print(f"{"N°":<3}.- {"nombre":<15} {"Clase":<10} {"nivel":<4} {"rango":<10}")
        for i in range(len(personajes)):
            print(f"{i+1<3}.- {personajes[i]["nombre"]:<20} {personajes[i]["Clase"] :<10} {personajes[i]["nivel"]:<4} {personajes[i]["rango"]:<10}")
    else:
        print("No hay personajes Registrados")