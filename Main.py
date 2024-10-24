import GestionAdmin
import GestionCliente
from Conexion import Conexion
from Iniciar import iniciar


def meterIdCliente():
    dni = input("Introduce tu DNI: ")
    sentencia = "SELECT * FROM usuario WHERE dni = %s"

    conexion = Conexion()
    cursor = conexion.getCursor()

    # Ejecuta la consulta pasando el valor del DNI como parámetro
    cursor.execute(sentencia, (dni,))

    respuesta = cursor.fetchone()
    conexion.close()
    if not respuesta :
        print("DNI no existente")
        opcion = input("Pulsa 1 para seguir cualquier otro para salir \t")
        if opcion != "1":
            return meterIdCliente()
        else:
            return (False,)
    else:
        dni = respuesta[0]
        nombre = respuesta[1]
        apellido = respuesta[2]
        pago = respuesta[3]
        moroso = respuesta[4]
        privilegio = respuesta[5]
        return True,dni,nombre,apellido,pago,moroso,privilegio

# admin 39114963J cliente 123456789A
aparatos, clientes = iniciar()

opcion = -1
while opcion != 0:

    opcion =  int(input("Bienvenidos al gym gymforthemoment, esta es la aplicación de gestión, elige una opción:\n"
                   "1. Registrarse\n"
                   "0. Salir\n"))
    match opcion:
        case 1:
            datos = meterIdCliente()
            if datos[0]:
                if datos[len(datos)-1]:
                    GestionAdmin.menu(datos[1], datos[2], datos[3])
                else:
                    GestionCliente.menu(datos[1], datos[2], datos[3], datos[4], datos[5])
        case 0:
            print("Saliendo...")
            
