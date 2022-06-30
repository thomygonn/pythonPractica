class Libro:
    def __init__(self):
        pass
    def registrar_libro(self,nombre):
        self.nombre = nombre
        print("sad")
    def _nuevo_libro(self):
        self.nombre = input()


if __name__ == "__main__":
    nuevoLibro = Libro()#parametro del nuevo)
    nuevoLibro.registrar_libro()#y todas las func
