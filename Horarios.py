class Horarios:
    horario = {
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

    def anyadirCliente(self,nombre, sesion):
        self.horario[sesion] = nombre


    def mostrarHorario(self):
        AUX=0
        for hora in self.horario:
            if hora%2==0:
                aux = "00"
            else:
                aux= "30"
            print((int)(hora/2),":",aux,self.horario[hora])