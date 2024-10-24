import GestionAdmin
import GestionCliente
from Conexion import Conexion
from Iniciar import iniciar


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

def registro():
    dni = input("Introduce el tu dni: ")
    sentencia = "Select * from usuarios where id = %s"
    base = Conexion()
    cursor = base.getCursor()
    cursor.execute(sentencia, (dni,))
    usuarioDatos = cursor.fetchone()
    return usuarioDatos

# Inicializamos los aparatos y clientes
aparatos, clientes = iniciar()

opcion = -1
while opcion != 0:

    opcion =  int(input("Bienvenidos al gym gymforthemoment, esta es la aplicación de gestión, elige una opción:\n"
                   "1. Registrarse\n"
                   "0. Salir\n"))
    match opcion:
        case 1:
            datos = registro()
            if(datos[5]):
                GestionAdmin.menu(datos[0],datos[1],datos[2])
            else:
                GestionCliente.menu(datos[0],datos[1],datos[2],datos[3],datos[4])
        case 0:
            print("Saliendo...")
            
