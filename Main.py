from Aparatos import Aparatos
from Cliente import Cliente

aparatos = Aparatos("jalon al pecho", 1)
cliente = Cliente("Pepe Jimenez Gomez")
aparatos.clientereserva(cliente, 23, 1)
aparatos.mostrarhorario(1)