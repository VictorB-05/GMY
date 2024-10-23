from Conexion import Conexion

Usuario = ""
def menu():
    opcion = -1
    while opcion != 0:
        opcion = int(input(f"Bienvenido al programa del admin {Usuario}\n"
               "1. Hacer recibo de pagos\n"
               "2. Morosos\n"
               "3. Añadir maquina\n"
               "4. Eliminar maquina\n"
               "5. Pagar\n"
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

    return None