from Aparatos import Aparatos
from Cliente import Cliente


def iniciar():
    # Creamos una lista de aparatos
    lista_aparatos = [
        Aparatos("Jalón al pecho", 1),
        Aparatos("Press de banca", 2),
        Aparatos("Sentadillas", 3),
        Aparatos("Remo en máquina", 4)
    ]

    # Creamos una lista de clientes
    lista_clientes = [
        Cliente("Pepe Jimenez Gomez", 1,False),
        Cliente("Maria Perez Lopez", 2,False),
        Cliente("Juan Carlos Sanchez Romero", 3,True),
        Cliente("Ana Maria Dominguez Gomez", 4,False),
        Cliente("Luis Martinez Ruiz", 5,False),
        Cliente("Laura Fernandez Diaz", 6,False),
        Cliente("Carlos Hernandez Ortega", 7,False),
        Cliente("Sofia Martinez Lopez", 8,True)
    ]

    # Asignamos algunos clientes a las máquinas, con sesiones y días distribuidos
    # Jalón al pecho
    lista_aparatos[0].clientereserva(lista_clientes[0], 23, 1)
    lista_aparatos[0].clientereserva(lista_clientes[1], 15, 2)
    lista_aparatos[0].clientereserva(lista_clientes[2], 10, 3)
    lista_aparatos[0].clientereserva(lista_clientes[3], 40, 4)
    lista_aparatos[0].clientereserva(lista_clientes[4], 35, 5)

    # Press de banca
    lista_aparatos[1].clientereserva(lista_clientes[1], 12, 1)
    lista_aparatos[1].clientereserva(lista_clientes[5], 18, 2)
    lista_aparatos[1].clientereserva(lista_clientes[6], 30, 3)
    lista_aparatos[1].clientereserva(lista_clientes[7], 22, 4)
    lista_aparatos[1].clientereserva(lista_clientes[0], 9, 5)

    # Sentadillas
    lista_aparatos[2].clientereserva(lista_clientes[2], 48, 1)
    lista_aparatos[2].clientereserva(lista_clientes[3], 25, 2)
    lista_aparatos[2].clientereserva(lista_clientes[4], 12, 3)
    lista_aparatos[2].clientereserva(lista_clientes[5], 32, 4)
    lista_aparatos[2].clientereserva(lista_clientes[6], 19, 5)

    # Remo en máquina
    lista_aparatos[3].clientereserva(lista_clientes[3], 35, 1)
    lista_aparatos[3].clientereserva(lista_clientes[4], 20, 2)
    lista_aparatos[3].clientereserva(lista_clientes[5], 10, 3)
    lista_aparatos[3].clientereserva(lista_clientes[7], 15, 4)
    lista_aparatos[3].clientereserva(lista_clientes[0], 42, 5)

    return lista_aparatos, lista_clientes