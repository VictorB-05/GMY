import GestionCliente
from Iniciar import iniciar

# Inicializamos los aparatos y clientes
aparatos, clientes = iniciar()

opcion = -1
while opcion != 0:

    opcion =  int(input("Bienvenidos al gym gymforthemoment, esta es la aplicación de gestión, elige una opción:\n"
                   "1. Menu Cliente\n"
                   "2. Menu Admin\n"
                   "0. Saliendo\n"))
    match opcion:
        case 1:
            GestionCliente.menu()

            """    # Solicitamos la opción del usuario
               opcion = input("Bienvenidos al gym gymforthemoment, esta es la aplicación de gestión, elige una opción:\n"
                               "1. Reservar aparato\n"
                               "2. Mirar horarios de los aparatos\n"
                               "3. Mirar recibo y quien ha pagado\n"
                               "0. Salir\n")

               # Convertimos la opción a entero
               opcion = int(opcion)
               match opcion:
                   case 1:
                       #Introducimos los datos para reservar el aparato
                       idAparato = int(input("Introduce el ID del aparato: "))
                       idCliente = int(input("Introduce tu ID de cliente: "))
                       dia = int(input(
                               "Introduce el día de la semana (1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes): "))
                       sesion = float(input("Introduce la hora de tu sesión (usa decimales, por ejemplo, 14.5 para 14:30): "))

                       if ((int)(sesion*2)) == sesion*2:
                           # Aseguramos que las conversiones están bien y los índices existen
                           if 1 <= idAparato <= len(aparatos) and 1 <= idCliente <= len(clientes):
                               if aparatos[idAparato - 1].clientereserva(clientes[idCliente - 1], sesion * 2, dia):
                                   print("Sesion intrpducida correctamente")
                               else:
                                   print("Sesion cogido mira el horario y elije otra")
                           else:
                               print("ID de aparato o cliente fuera de rango")
                       else:
                           print("La hora tiene que ser numero entero o medio")

                   case 2:
                       #introducimos los datos para ver el horario de un aprato
                       idAparato = int(input("Introduce el ID del aparato: "))
                       dia = int(input(
                           "Introduce el día de la semana (1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes): "))
                       if 1 <= idAparato <= len(aparatos):
                           aparatos[idAparato - 1].mostrarhorario(dia)
                       else:
                           print("ID de aparato fuera de rango")

                   case 3:
                       for cliente in clientes:
                           print(cliente.pagar())

                   case 0:
                       print("Saliendo...")

                   case _:
                       print("Opción no encontrada, inténtalo de nuevo")"""