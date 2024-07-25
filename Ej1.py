class Alumno:
    def __init__(self, Nombre, Apellido, Edad, Curso):
        self.nombre = Nombre.capitalize()
        self.apellido = Apellido.capitalize()
        self.edad = Edad
        self.curso = Curso
    
    def programar(self):
        return print(f"El alumno {self.nombre} esta programando")
    
alumno1 = Alumno(input("Ingrese su Nombre:"), input("Ingrese su Apellido:"), int(input("Ingrese su Edad:")), input("Ingrese su Curso:"))
alumno1.programar()