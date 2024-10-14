from Horarios import Horarios


class Aparatos:

    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id
        self.lunes = Horarios()
        self.martes = Horarios()
        self.miercoles = Horarios()
        self.jueves = Horarios()
        self.viernes = Horarios()

    def clientereserva(self, cliente, hora, dia):
        match dia:
            case 1:
                self.lunes.anyadirCliente(cliente, hora)
            case 2:
                self.martes.anyadirCliente(cliente, hora)
            case 3:
                self.miercoles.anyadirCliente(cliente, hora)
            case 4:
                self.jueves.anyadirCliente(cliente, hora)
            case 5:
                self.viernes.anyadirCliente(cliente, hora)

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