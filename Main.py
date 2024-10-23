import GestionAdmin
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
        case 2:
            GestionAdmin.menu()