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
        Cliente("Pepe Jimenez Gomez", 1),
        Cliente("Maria Perez Lopez", 2),
        Cliente("Juan Carlos Sanchez", 3),
        Cliente("Ana Maria Dominguez", 4)
    ]

    # Asignamos algunos clientes a las máquinas con sesiones y días aleatorios
    lista_aparatos[0].clientereserva(lista_clientes[0], 23, 1)  # Pepe reserva Jalón al pecho
    lista_aparatos[1].clientereserva(lista_clientes[1], 12, 3)  # Maria reserva Press de banca
    lista_aparatos[2].clientereserva(lista_clientes[2], 48, 5)  # Juan reserva Sentadillas
    lista_aparatos[3].clientereserva(lista_clientes[3], 35, 2)  # Ana reserva Remo en máquina

    return lista_aparatos, lista_clientes