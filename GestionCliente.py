from datetime import time

import Conexion

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
                idAparato = meterIdAparato()
                idCliente = meterIdCliente()
                dia = int(input(
                    "Introduce el día de la semana (1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes): "))
                if (dia<1) or (dia>5):
                    raise Exception("Dia incorrecto");

                sesionh = int(input("Introduce la hora de tu sesión"))

                if(int(input("Si quieres a empunto pon 0 si queires a y media pon 1"))==1):
                    hora = time(sesionh, 30)
                else:
                    hora= time(sesionh,0)



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
    sentencia = f"Select id from aparato where id = {clave}"
    respuesta = Conexion.Conexion(sentencia)
    if not respuesta:
        print("Id no existente")
        return meterIdAparato()
    return clave

def meterIdCliente():
    clave = input(f"Introduce tu DNI: ")
    sentencia = f"Select DNI from usuario where DNI = '{clave}'"
    respuesta = Conexion.Conexion(sentencia)
    print(respuesta.fetchall())
    if not respuesta:
        print("DNI no existente")
        return meterIdCliente()
    return clave

def comprobarSesion(DNI, Idaparato, hora, dia):
    sentencia = f"Select * from reservas where DNI = {DNI} AND where "
    respuesta = Conexion.Conexion(sentencia)