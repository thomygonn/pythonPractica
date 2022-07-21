
from libros import lista_libros

class Biblioteca:
    def __init__(self,nomLibreria):
        self.nomLibreria= nomLibreria
        self._libros = []
    
    def agregar_libro(self):
        nombre = input("Ingrese el nombre del libro a registrar: ")
        autor = input("Ingrese el nombre del autor: ")
        fechaPublicacion= input("Ingrese la fecha de publicacion: ")
        list(lista_libros.append({
            nombre,autor,fechaPublicacion            
        }))
        
    def consultar_libros(self):
        for claves in lista_libros:
            for i in claves:
                print(claves[i])
                print(lista_libros[1])
        

    def quitar_libro(self):
        print()

    menu_libros=(agregar_libro,consultar_libros,quitar_libro)

""" class Libro:
    def __init__(self):
        pass
    def __nombre__(self,nombre_lib,autor_lib,fechaPub_lib):
        self.nombre_libro = nombre_lib
        self.autor_lib = autor_lib
        self.fechaPub = fechaPub_lib """


biblioteca = Biblioteca("Genos")
print(Biblioteca.presentacion)
Biblioteca.agregar_libro(lista_libros)
""" Biblioteca.consultar_libros(lista_libros) """
