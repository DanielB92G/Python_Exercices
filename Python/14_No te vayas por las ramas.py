class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [r + 1 for r in self.ramas]

    def quitar_rama(self, pos: int):
        if 0 <= pos < len(self.ramas):
            self.ramas.pop(pos)
        else:
            raise IndexError("Posicion de rama no valida")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "num_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas,
        }


arbol = Arbol()
arbol.crecer_tronco()
arbol.nueva_rama()
arbol.crecer_ramas()
arbol.nueva_rama()
arbol.nueva_rama()
arbol.quitar_rama(2)
print(arbol.info_arbol())
