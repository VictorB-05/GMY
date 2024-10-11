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
                self.lunes.mostrarHorario()
            case 2:
                self.martes.mostrarHorario()
            case 3:
                self.miercoles.mostrarHorario()
            case 4:
                self.jueves.mostrarHorario()
            case 5:
                self.viernes.mostrarHorario()