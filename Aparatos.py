from xmlrpc.client import Boolean

from Horarios import Horarios


class Aparatos:

    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id
        # dentro del constructor para que no sea estatico y sea diferente por cada objeto
        self.lunes = Horarios()
        self.martes = Horarios()
        self.miercoles = Horarios()
        self.jueves = Horarios()
        self.viernes = Horarios()

    def clientereserva(self, cliente, hora, dia):
        aux = Boolean
        match dia:
            case 1:
                aux = self.lunes.anyadirCliente(cliente, hora)
            case 2:
                aux = self.martes.anyadirCliente(cliente, hora)
            case 3:
                aux = self.miercoles.anyadirCliente(cliente, hora)
            case 4:
                aux = self.jueves.anyadirCliente(cliente, hora)
            case 5:
                aux = self.viernes.anyadirCliente(cliente, hora)
        return aux

    def mostrarhorario(self, dia):
        match dia:
            case 1:
                print(f"Horarios del lunes de la maquina {self.tipo} id {self.id}")
                self.lunes.mostrarHorario()
            case 2:
                print(f"Horarios del martes de la maquina {self.tipo} id {self.id}")
                self.martes.mostrarHorario()
            case 3:
                print(f"Horarios del miercoles de la maquina {self.tipo} id {self.id}")
                self.miercoles.mostrarHorario()
            case 4:
                print(f"Horarios del jueves de la maquina {self.tipo} id {self.id}")
                self.jueves.mostrarHorario()
            case 5:
                print(f"Horarios del viernes de la maquina {self.tipo} id {self.id}")
                self.viernes.mostrarHorario()