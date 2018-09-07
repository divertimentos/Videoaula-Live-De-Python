class Passaro:
    estado = "indefinido"

    def voar(self):
        self.estado = "voando"
        print(self.estado)
    
    def pousar(self):
        self.estado = "parado"
        print(self.estado)

aguia = Passaro()
print(aguia.pousar())
print(aguia.estado)
