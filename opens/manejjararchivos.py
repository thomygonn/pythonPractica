from io import open

""" archivo_textos = open('archivo.txt','w')

frase = "Lindo dia para encerrarse \n a estudiar Python "

archivo_textos.write(frase) """


#read

""" archivo_textos = open("archivo.txt",'r')

texto = archivo_textos.read() 

archivo_textos.close()

print(texto) """ #leyendo 


#readlines
""" archivo_textos = open("archivo.txt",'r')

lineas_texto = archivo_textos.readlines()

print(lineas_texto[0]) """


#append
archivo_textos = open("archivo.txt",'w') #a de append o agregar

archivo_textos.write(str({"nombre" : "Harry Potter y la piedra filosofal","autor":"J.K. Rowling","fecha_publicacion":"1997/02/01"}))

archivo_textos.write(str({"nombre": "Asi habló Zaratustra",
    "autor":"Friederich Nietzche",
    "fecha_publicacion":"1885/03/06"
    },))
archivo_textos.write(str({"nombre":"Mi planta de naranja lima",
    "autor":"Jose Mauro de Vasconcelos",
    "fecha_publicacion":"1968/12/02"}))

archivo_textos.write(str({"nombre":"El hombre mas rico de Babilonia",
    "autor": "George Samuel Clason",
    "fecha_publicacion":"1926/06/15"  
    }))
archivo_textos.write(str({"nombre":"Humano, demasiado humano",
    "autor":"Friederich Nietzche",
    "fecha_publicacion":"1878/12/12"   
    }))

for a in archivo_textos:
    print(f"Listado libros :", "\n", archivo_textos[a])

archivo_textos = open("archivo.txt","r")
print(archivo_textos.read())

