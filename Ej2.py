class Mago:
    def __init__(self, Hechizo):
        self.hechizo = Hechizo

    def mostrar_hechizo(self):
        print(f"El usuario tiene un hechizo especial llamado:{self.hechizos}.")

class Guerrero:
    def __init__(self, Defensa):
        self.defensa = Defensa

    def mostrar_defensa(self):
        print(f"El usuario tiene {self.defensa} de defensa.")

class Elfo:
    def __init__(self, Aura):
        self.aura = Aura

    def mostrar_aura(self):
        print(f"El usuario tiene {self.aura} de Aura.")

class DarkLord(Guerrero, Elfo, Mago):
    def __init__(self, Defensa, Aura, Hechizo, poder):
        Guerrero.__init__(self, Defensa)
        Elfo.__init__(self, Aura)
        Mago.__init__(self, Hechizo)
        self.poder = poder

    def Stats(self):
        print(f"Dark Lord tiene {self.defensa} DEF, {self.aura} AURA, un poderoso hechizo llamado:{self.hechizo} {self.poder} Poder")

jefeSup = DarkLord(int(input("Ingrese su Defensa:")), int(input("Ingrese su Aura:")), input("Ingrese su Hechizo más poderoso:"), int(input("Ingrese su Poder:")))
jefeSup.Stats()
jefeSup.mostrar_aura()