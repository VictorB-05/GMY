from Horarios import Horarios


class Aparatos:
    lunes = Horarios()
    martes = Horarios()
    miercoles = Horarios()
    jueves = Horarios()
    viernes = Horarios()

    def __init__(self, tipo, id):
        self.tipo = tipo
        self.id = id

    def clientereserva(self, cliente, hora, dia):
        match dia:
            case 1:
                self.lunes.anyadirCliente(cliente.nombre, hora)
            case 2:
                self.martes.anyadirCliente(cliente.nombre, hora)
            case 3:
                self.miercoles.anyadirCliente(cliente.nombre, hora)
            case 4:
                self.jueves.anyadirCliente(cliente.nombre, hora)
            case 5:
                self.viernes.anyadirCliente(cliente.nombre, hora)

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