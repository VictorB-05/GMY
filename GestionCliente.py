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
                idAparato = meterIds("Aparato","id")
                idCliente = meterIds("Usuario","DNI")
                dia = int(input(
                    "Introduce el día de la semana (1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes): "))
                sesion = float(input("Introduce la hora de tu sesión (usa decimales, por ejemplo, 14.5 para 14:30): "))

                if ((int)(sesion * 2)) == sesion * 2:
                    # Aseguramos que las conversiones están bien y los índices existen
                    sesion*2
                else:
                    print("La hora tiene que ser numero entero o medio")

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

def meterIds(tabla,id):
    clave = input(f"Introduce la ID de {tabla}: ")
    sentencia = f"Select {id} from {tabla} where {id} = {clave}"
    print(sentencia)
    respuesta = Conexion.Conexion(sentencia)
    if not respuesta:
        print("Id no existente")
        return meterIds(tabla, id)
    return clave