class Cliente:
    def __init__(self, nombre,numeroSocio,moroso):
        self.nombre = nombre
        self.moroso = moroso
        self.numeroSocio = numeroSocio

    def pagar (self):
        if self.moroso:
            return self.numeroSocio,self.nombre,"Debe pagar"
        else:
            return self.numeroSocio,self.nombre,"Ha pagado"