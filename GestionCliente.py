from datetime import time
from Conexion import Conexion

Usuario = ""
def menu():
    print("SAS")
    opcion = -1
    while opcion != 0:
        opcion = int(input(f"Bienvenido al programa del cliente {Usuario}\n"
              "1. Apuntarse a maquina\n"
              "2. "))
        match opcion:
            case 1:
                # Introducimos los datos para reservar el aparato
                idCliente = meterIdCliente()
                idAparato = meterIdAparato()
                dia = int(input(
                    "Introduce el día de la semana (1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes): "))
                if (dia<1) or (dia>5):
                    raise Exception("Dia incorrecto")

                sesionh = int(input("Introduce la hora de tu sesión si quieres media hora pon un 0,5"))
                sesionm = (sesionh*10)%10

                if sesionm == 0.5 :
                    hora = time(sesionh, 30)
                elif sesionm == 0 :
                    hora= time(sesionh,0)
                else:
                    print("Hora incorrecta o X,0 o X,5")


            case 2:
                # introducimos los datos para ver el horario de un aprato
                idAparato = int(input("Introduce el ID del aparato: "))
                dia = int(input(
                    "Introduce el día de la semana (1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes): "))
    return None
def registro():
    usuario = input("Introduce el tu id: ")
    sentencia = "Select * from usuarios where id = ",usuario
    base = Conexion.Conexion(sentencia)
    print(base.fetchone())

def comprobarExstencia(dato, nombreDato,tabla):
    sentencia = f"Select {nombreDato} from {tabla} where {nombreDato} = {dato};"
    respuesta = Conexion.Conexion(sentencia)
    if not respuesta:
        return False
    else:
        return True

def meterIdAparato():
    clave = input(f"Introduce la ID del aparato: ")
    sentencia = "SELECT id FROM aparato WHERE id = %s"

    conexion = Conexion()
    cursor = conexion.getCursor()

    cursor.execute(sentencia, (clave,))

    # Ejecuta la consulta pasando el valor del DNI como parámetro
    respuesta = cursor.fetchone()
    conexion.close()
    if not respuesta:
        print("Id no existente")
        return meterIdAparato()
    return clave

def meterIdCliente():
    dni = input("Introduce tu DNI: ")
    sentencia = "SELECT dni FROM usuario WHERE dni = %s"

    conexion = Conexion()
    cursor = conexion.getCursor()

    # Ejecuta la consulta pasando el valor del DNI como parámetro
    cursor.execute(sentencia, (dni,))

    respuesta = cursor.fetchall()
    conexion.close()
    if not respuesta :
        print("DNI no existente")
        return meterIdCliente()
    return respuesta

def comprobarSesion(DNI, Idaparato, hora, dia):
    sentencia = f"Select * from reservas where dni = {DNI} AND where "
    respuesta = Conexion.Conexion(sentencia)