from contextlib import nullcontext
from datetime import time

from Conexion import Conexion

Usuario = ""
def menu():
    opcion = -1
    while opcion != 0:
        opcion = int(input(f"Bienvenido al programa del cliente {Usuario}\n"
              "1. Apuntarse a maquina\n"
              "2. Ver horarios\n"
              "3. Ver tus reservas\n"
              "4. Cancelar tus reservas\n"
              "5. Pagar\n" ))
        match opcion:
            case 1:
                # Introducimos los datos para reservar el aparato
                idCliente = meterIdCliente()
                idAparato = meterIdAparato()
                dia = int(input(
                    "Introduce el día de la semana (1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes): "))
                if (dia<1) or (dia>5):
                    raise Exception("Dia incorrecto")

                sesionh = float(input("Introduce la hora de tu sesión si quieres media hora pon un 0.5"))
                sesionm = (sesionh*10)%10

                # Verificamos si la hora es redonda (X.0) o tiene media hora (X.5)
                if sesionh.is_integer():
                    hora = time(int(sesionh), 0)  # Sesión redonda (X.0)
                    print(comprobarSesion(idCliente, idAparato, dia, hora.isoformat()))
                elif sesionh == int(sesionh) + 0.5:
                    hora = time(int(sesionh), 30)  # Sesión con media hora (X.5)
                    print(comprobarSesion(idCliente, idAparato, dia, hora.isoformat()))
                else:
                    print("Hora incorrecta, debe ser X.0 o X.5")

            case 2:
                idAparato = meterIdAparato()
                dia = int(input(
                    "Introduce el día de la semana (1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes): "))
                if (dia < 1) or (dia > 5):
                    raise Exception("Dia incorrecto")
                sentencia = ("SELECT hora, usuario.nombre FROM reservas "
                            "INNER JOIN usuario ON reservas.dni = usuario.dni "
                            "WHERE dia = %s AND id_aparato = %s")
                conexion = Conexion()
                cursor = conexion.getCursor()

                cursor.execute(sentencia, (dia,idAparato))

                resultado = cursor.fetchall()
                print(f"Reservas para el aparato {idAparato} en el día {dia}:")
                for reserva in resultado:
                    hora = reserva[0]
                    if(reserva[1] == ""):
                        usuario == "Vacio"
                    else:
                        usuario = reserva[1]
                    print(f"Hora: {hora} - Usuario: {usuario}")
            case 5:
                dni = meterIdCliente()
                sentencia = "SELECT pago,moroso FROM usuario WHERE dni = %s"

                conexion = Conexion()
                cursor = conexion.getCursor()

                # Ejecuta la consulta pasando el valor del DNI como parámetro
                cursor.execute(sentencia, (dni,))

                resultado = cursor.fetchone()
                pago = resultado[0]
                moroso = resultado[1]
                conexion.close()
                print(pago)
                if pago:
                    print("Has pagado")
                elif moroso:
                    print("No has pagado meses atrasados, pagar")
                    opcion = int(input("1. Pagar\n" "2. Salir"))
                    if opcion == 1:
                        print("sas")
                        sentencia = "UPDATE usuario SET pago=1, moroso=0  WHERE dni = %s"

                        conexion = Conexion()
                        cursor = conexion.getCursor()

                        # Ejecuta la consulta pasando el valor del DNI como parámetro
                        cursor.execute(sentencia, (dni,))
                        conexion.commit()
                        conexion.close()
                else :
                    print("No has pagado aun el mes")
                    opcion = input("1. Pagar\n" "2. Salir")
                    if opcion == 1:
                        sentencia = "UPDATE usuario SET pago=1 WHERE dni = %s"

                        conexion = Conexion()
                        cursor = conexion.getCursor()

                        # Ejecuta la consulta pasando el valor del DNI como parámetro
                        cursor.execute(sentencia, (dni,))
                        conexion.commit()
                        conexion.close()




    return None
def registro():
    usuario = input("Introduce el tu id: ")
    sentencia = "Select * from usuarios where id = ",usuario
    base = Conexion.Conexion(sentencia)
    print(base.fetchone())

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
    return dni

def comprobarSesion(dni, Idaparato,dia , hora):
    print(hora,dia,Idaparato,dni)
    sentencia = "SELECT id FROM reservas WHERE id_aparato = %s AND dia = %s AND hora = %s"
    conexion = Conexion()
    cursor = conexion.getCursor()
    # Ejecuta la consulta pasando el valor del DNI como parámetro
    cursor.execute(sentencia, (Idaparato,dia,hora))

    respuestaAparato = cursor.fetchall()
    conexion.close()

    sentencia = "SELECT dni FROM reservas WHERE dni = %s AND dia = %s AND hora = %s"
    conexion = Conexion()
    cursor = conexion.getCursor()
    # Ejecuta la consulta pasando el valor del DNI como parámetro
    cursor.execute(sentencia, (dni, dia, hora))

    respuestaCliente = cursor.fetchall()
    conexion.close()

    # Verificar si no hay reservas ni para el aparato ni para el cliente en ese horario
    if not respuestaAparato and not respuestaCliente:  # Ambas respuestas deben ser listas vacías
        sentencia_insertar = "INSERT INTO reservas (dni, id_aparato, dia, hora) VALUES (%s,%s,%s,%s)"
        conexion = Conexion()
        cursor = conexion.getCursor()
        cursor.execute(sentencia_insertar, (dni, Idaparato, dia, hora))
        conexion.commit()#para introducir la sentencia hay que hacer un commit()
        conexion.close()
        return "Sesión iniciada"
    else:
        return "Aparato ocupado o el cliente ya tiene una reserva en ese horario"
