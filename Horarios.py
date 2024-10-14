from xmlrpc.client import Boolean


class Horarios:
    def __init__(self):
        # dentro del constructor para que no sea statico y sea diferente por cada objeto
        self.horario = {
            1: "Vacio",
            2: "Vacio",
            3: "Vacio",
            4: "Vacio",
            5: "Vacio",
            6: "Vacio",
            7: "Vacio",
            8: "Vacio",
            9: "Vacio",
            10: "Vacio",
            11: "Vacio",
            12: "Vacio",
            13: "Vacio",
            14: "Vacio",
            15: "Vacio",
            16: "Vacio",
            17: "Vacio",
            18: "Vacio",
            19: "Vacio",
            20: "Vacio",
            21: "Vacio",
            22: "Vacio",
            23: "Vacio",
            24: "Vacio",
            25: "Vacio",
            26: "Vacio",
            27: "Vacio",
            28: "Vacio",
            29: "Vacio",
            30: "Vacio",
            31: "Vacio",
            32: "Vacio",
            33: "Vacio",
            34: "Vacio",
            35: "Vacio",
            36: "Vacio",
            37: "Vacio",
            38: "Vacio",
            39: "Vacio",
            40: "Vacio",
            41: "Vacio",
            42: "Vacio",
            43: "Vacio",
            44: "Vacio",
            45: "Vacio",
            46: "Vacio",
            47: "Vacio",
            48: "Vacio",
        }

    def anyadirCliente(self,cliente, sesion):
        if self.horario[sesion] == "Vacio":
            self.horario[sesion] = cliente
            aux = True
        else:
            aux = False
        return aux


    def mostrarHorario(self):
        for hora in self.horario:
            if self.horario[hora] == "Vacio":
                auxH = "Vacio"
            else:
                auxH = self.horario[hora].nombre
            if hora%2==0:
                aux = "00"
            else:
                aux= "30"
            if hora/2<10:
                #0,
                print(f"0{(int)(hora / 2)}:{aux}",auxH)
            else:
                print(f"{(int)(hora / 2)}:{aux}", auxH)