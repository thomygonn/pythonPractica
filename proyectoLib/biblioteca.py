
class Biblioteca:
    def __init__(self,nomLibreria):
        self.nomLibreria= nomLibreria
        self._libros = []
    def presentacion(self):
        print("Bienvenido a la biblioteca",self.nomLibreria)
    def agregar_libro(self,libros):
        self._libros.append({
            libro.titulo,
            libro.autor,
            libro.fechaPub,
        })

    def consultar_libros(self):
        return self._libros

    def consultar_libro(self, id):
        return self._libros[id]

    def quitar_libro(self, id):
        self._libros.pop(id)

    registrar_libro=(agregar_libro,consultar_libros,quitar_libro)

class Libro:
    def __init__(self):
        pass
    def __nombre__(self,nombre_lib,autor_lib,fechaPub_lib):
        self.nombre_libro = nombre_lib
        self.autor_lib = autor_lib
        self.fechaPub = fechaPub_lib


biblioteca = Biblioteca("Genos")
print(Biblioteca.presentacion)

