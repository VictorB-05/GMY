from Conexion import Conexion

Usuario = ""
def menu(dni,nombre,apellidos):
    opcion = -1
    while opcion != 0:
        opcion = int(input(f"Bienvenido al programa del admin {Usuario}\n"
                "1. Hacer recibo de pagos\n"
                "2. Morosos\n"
                "3. Añadir maquina\n"
                "4. Eliminar maquina\n"
                "5. Dar de alta cliente\n"
                "6. Dar de baja cliente\n"
                "0. Salir\n"))
        match opcion:
            case 1:
                sentencia = "SELECT dni,pago,moroso FROM usuario WHERE privilegios = False"

                conexion = Conexion()
                cursor = conexion.getCursor()
                cursor.execute(sentencia)
                resultado = cursor.fetchall()
                conexion.close()

                conexion = Conexion()
                cursor = conexion.getCursor()
                for cliente in resultado:
                    dni = cliente[0]
                    pago = cliente[1]
                    moroso = cliente[2]
                    print(dni)
                    if pago:
                        sentencia = "UPDATE usuario SET pago=0, moroso=0  WHERE dni = %s"
                    elif not moroso:
                        sentencia = "UPDATE usuario SET pago=0, moroso=1  WHERE dni = %s"
                    else:
                        print(f"El usuario {dni} lleva varios meses sin pagar")
                        sentencia = "UPDATE usuario SET pago=0, moroso=1  WHERE dni = %s"
                    print(sentencia)
                    cursor.execute(sentencia, (dni,))
                actualizar = int(input("¿Seguro que quieres actualizar tu database?\n"
                                       "1. Si\n" "2. No, salir\n"))
                if actualizar == 1:
                    conexion.commit()
                conexion.close()
            case 2:
                sentencia = "SELECT dni,nombre,apellidos FROM usuario WHERE moroso = TRUE"
                conexion = Conexion()
                cursor = conexion.getCursor()
                cursor.execute(sentencia)
                resultado = cursor.fetchall()
                conexion.close()
                print("Morosos:")
                for cliente in resultado:
                    dni = cliente[0]
                    nombre = cliente[1]
                    apellidos = cliente[2]
                    print("DNI:",dni,"Nombre:",nombre,apellidos)
            case 3:
                nombre = input("Introduce el nombre del aparato: ")
                sentencia = "INSERT INTO aparato (nombre) VALUES (%s)"
                conexion = Conexion()
                cursor = conexion.getCursor()
                cursor.execute(sentencia,(nombre,))
                conexion.commit()
                sentencia = "SELECT id FROM aparato WHERE nombre = %s"
                cursor = conexion.getCursor()
                cursor.execute(sentencia, (nombre,))
                resultado = cursor.fetchone()
                print("El id del nuevo aparato es {}".format(resultado[0]))
            case 4:
                clave = input(f"Introduce la ID del aparato: ")
                sentencia = "SELECT id,nombre FROM aparato WHERE id = %s"

                conexion = Conexion()
                cursor = conexion.getCursor()

                cursor.execute(sentencia, (clave,))

                # Ejecuta la consulta pasando el valor del DNI como parámetro
                respuesta = cursor.fetchone()

                if not respuesta:
                    print("Id no existente")
                else:
                    print("Seguro que quieres eliminar al aparto {} de la aplicación y todas sus reservas".format(respuesta[1]))
                    opcion = input("Pulsa 1 para si cualquier otro para no")
                    if opcion == "1":
                        sentencia= "DELETE FROM aparato WHERE id = %s"
                        cursor.execute(sentencia, (clave,))
                        conexion.commit()
                    else:
                        print("Acción cancelada")
                conexion.close()
            case 5:
                conexion = Conexion()
                cursor = conexion.getCursor()
                resultado = dniExixte(cursor)
                if resultado[1]:
                    print("Dni existente en la base de datos")
                else:
                    dni = resultado[0]
                    nombre = input("Introduce el nombre del cliente:\t")
                    apellidos = input("Introduce los apellidos del cliente:\t")
                    sentencia = "INSERT INTO usuario (dni,nombre,apellidos) VALUES (%s,%s,%s)"

                    cursor.execute(sentencia, (dni,nombre,apellidos))
                    conexion.commit()
                conexion.close()
            case 6:
                conexion = Conexion()
                cursor = conexion.getCursor()
                resultado = dniExixte(cursor)
                if resultado[1]:
                    datos = resultado[0]
                    print(f"DNI: {datos[0]} NOMBRE {datos[1]} APELLIDOS {datos[2]} ")
                    if datos[3]:
                        print("PAGO realizado")
                    else:
                        print("PAGO no hecho")

                    if datos[4]:
                        print("ES MOROSO/A")
                    else:
                        print("LLEVA LOS PAGOS AL DIA")


                    print("Seguro que quieres eliminar al cliente de la aplicación y todas sus reservas")
                    opcion = input("Pulsa 1 para si cualquier otro para no \t")
                    if opcion == "1":
                        sentencia = "DELETE FROM usuario WHERE dni = %s"
                        cursor.execute(sentencia, (datos[0],))
                        conexion.commit()
                        print("ELIMINADO CORRECTAMENTE")
                    else:
                        print("Acción cancelada")

                else:
                    print("Dni no existente en la base de datos")

                conexion.close()

    return None
def dniExixte(cursor):
    dni = input("Introduce el DNI del la persona:\t")
    sentencia = "SELECT * FROM usuario WHERE dni = %s"
    cursor.execute(sentencia,(dni,))
    resultado = cursor.fetchone()
    if not resultado:
        return dni,False
    return resultado,True
