from datetime import time
from Conexion import Conexion

def menu(dni,nombre,apellidos,pago,moroso):
    opcion = -1
    while opcion != 0:
        opcion = int(input(f"Bienvenido al programa del cliente {nombre} {apellidos}\n"
                "1. Apuntarse a maquina\n"
                "2. Ver horarios\n"
                "3. Ver tus reservas\n"
                "4. Cancelar tus reservas\n"
                "5. Pagar\n" 
                "0. Salir\n"))
        match opcion:
            case 1:
                # Introducimos los datos para reservar el aparato
                idAparato = meterIdAparato()
                dia = int(input(
                    "Introduce el día de la semana (1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes): "))
                if (dia<1) or (dia>5):
                    raise Exception("Dia incorrecto")

                sesionh = float(input("Introduce la hora de tu sesión si quieres media hora pon un 0.5"))
                # Verificamos si la hora
                if sesionh.is_integer():
                    hora = time(int(sesionh), 0)  # Sesión a empuento
                    print(comprobarSesion(dni, idAparato, dia, hora.isoformat()))
                elif sesionh == int(sesionh) + 0.5:
                    hora = time(int(sesionh), 30)  # Sesión a y media
                    print(comprobarSesion(dni, idAparato, dia, hora.isoformat()))
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
                        usuarioAux == "Vacio"
                    else:
                        usuarioAux = reserva[1]
                    print(f"Hora: {hora} - Usuario: {usuarioAux}")

            case 3:
                resultado = reservasUsuario(dni)
                print(f"Estas son tus reservas:")
                for reserva in resultado:
                    dia = reserva[0]
                    hora = reserva[1]
                    aparato = reserva[2]
                    print(f"Día: {dia} - Hora: {hora} - Aparato: {aparato}")

            case 4:
                resultado = reservasUsuario(dni)
                for i in range(0, len(resultado)):
                    dia = resultado[i][0]
                    hora = resultado[i][1]
                    aparato = resultado[i][2]
                    print(f"{i+1}. Día: {dia} - Hora: {hora} - Aparato: {aparato}")
                opcion = int(input("Numero de la sesión a eliminar"))-1
                if len(resultado) > opcion > 0:
                    sentencia = "DELETE FROM reservas WHERE id = %s"

                    conexion = Conexion()
                    cursor = conexion.getCursor()

                    # Ejecuta la consulta pasando el valor del DNI como parámetro
                    cursor.execute(sentencia, (resultado[opcion][3],))
                    conexion.commit()
                    conexion.close()
                else:
                    print("Error reserva no existente en la lista")
            case 5:
                if pago:
                    print("Has pagado")
                elif moroso:
                    print("No has pagado meses atrasados, pagar")
                    opcion = int(input("1. Pagar\n" "2. Salir"))
                    if opcion == 1:
                        sentencia = "UPDATE usuario SET pago=1, moroso=0  WHERE dni = %s"

                        conexion = Conexion()
                        cursor = conexion.getCursor()

                        # Ejecuta la consulta pasando el valor del DNI como parámetro
                        cursor.execute(sentencia, (dni,))
                        conexion.commit()
                        conexion.close()
                        pago = True
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
                        pago = True
                        moroso = False
    return None

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

def comprobarSesion(dni, Idaparato,dia , hora):
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
        conexion.commit()
        conexion.close()
        return "Sesión iniciada"
    else:
        return "Aparato ocupado o el cliente ya tiene una reserva en ese horario"

def reservasUsuario(dni):
    sentencia = ("SELECT dia, hora, aparato.nombre, reservas.id FROM reservas "
                 "INNER JOIN aparato ON reservas.id_aparato = aparato.id "
                 "WHERE dni = %s")
    conexion = Conexion()
    cursor = conexion.getCursor()

    cursor.execute(sentencia, (dni,))

    return cursor.fetchall()