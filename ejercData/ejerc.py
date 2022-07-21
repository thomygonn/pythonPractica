#*Ejercicios Tipo de datos simples:*

#1.- Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
def saludar():
    print('Hola mundo')
saludar()
#2.- Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
def enVariable():
    hola = 'Hola Mundo'
    print(hola)
enVariable()

#3.- Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
def horasTrabajadas():
    horas = int(input('Cuantas horas trabajaste? '))
    costo_hora = float(input('Cuanto cuesta tu hora? '))
    print (f'Tu salario es de :',horas * costo_hora)
#horasTrabajadas()


#4.- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales
def calcular_peso():
    peso = int(input('Ingrese su peso'))
    estatura = int(input('Ingrese su altura'))
    print(f'Tu indice de masa corporal es: ',peso * estatura /2)
#calcular_peso()

#5.- Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total
def panaderia ():
    barra = 3.49
    barra_ayer = 3.49*0.6
    vendidas_ayer = int(input('Ingrese el numero de barras vendidas de ayer'))
    vendidas_hoy = int(input('Ingrese el numero de barras vendidas hoy'))
    print(f'La barra de pan sale', barra , 'el descuento por no ser del dia es del 60% y queda con un precio de', barra_ayer, 'y la cantidad total de ventas es ', str(vendidas_ayer + vendidas_hoy) )
#panaderia()

#*Ejercicios Condicionales*

#1.- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def mayor_edad():
    edad = int(input('Ingrese su edad: '))
    if edad < 18:
        print('Es menor de edad')
    else:
        print('Es mayor de edad')
#mayor_edad()

#2.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
def contra():
    contraseña = '1234'
    cont = input('Ingrese la contraseña')
    if cont == contraseña:
        print('Acertaste la contraseña ')
    else:
        print('Recargue la pagina y vuelva a intentar')
#contra()

#3.- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

def esPar():
    numero = int(input('Ingrese su número: '))
    if numero // 2 == 0:
        print('Es par')
    else:
        print('Es inpar')
#esPar()

#4.- Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

def calc_entradas():
    edad = int(input('Ingrese su edad'))
    if edad < 4:
        print('Pase gratis')
    elif edad > 4 and edad <18:
        print('Debe abonar 5 euros')
    else:
        print('Debe abonar 10 euros')
#calc_entradas()

#5.- Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


#*Ejercicios Bucles*

#1.- Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
def pedir_palabra():
    palabra = input('Ingrese una palabra')
    for x in range(10):
        print(palabra)
#pedir_palabra()

#2.- Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
def pedir_num():
    numero = int(input('Ingrese un número: '))
    for x in range(1,numero+1):
        print(x)
#pedir_num()

#3.- Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10
def multiply():
    num = int(input('Ingrese un número: '))
    for x in (range(1,11)):
        print(x * num)
#multiply()

#4.- Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
def adivinar_contra():
    contraseña = 'qwerty'
    cont = ''
    while cont != contraseña:
        cont = input('Ingrese una contraseña')
        if cont == contraseña:
            print('Adivinaste !!!!')
    

#adivinar_contra()

#5.- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase

def frase_letra():
    frase = input('Ingrese una frase: ')
    letra = input('Ingrese una letra: ')
    cont=0
    for i in frase:
        if i==letra:
            cont+=1   
        else:
            pass
    print('La cantidad de letras es ', cont)
frase_letra()       


