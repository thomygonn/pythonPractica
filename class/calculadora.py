class calculadora:

    def __init__(self,id,botones,marca):
        self.id=id
        self.botones=botones
        self._marca=marca
    
    def bienvenida(self):
        return "Bienvenido a la calculadora"

    def suma(self, a, b):
        return a + b
    def resta(a, b):
        return a - b
    def multiplicar(a, b):
        return a * b
    def dividir(a, b):
        return a / b



        

class persona:
    
    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def presentarse(self):
        print("hola! soy", self.nombre, " ", self.apellido, " y tengo ", self.edad, "años." )


class empleado(persona):
    def __init__(self, nombre, apellido, edad, sector):
        super().__init__(nombre, apellido, edad)
        self.sector=sector

    def hacerseElPiola(self):
        print("soy re piola por que manejo todo: ", self.sector)


#class gerente(persona)

alan = empleado("alan", "benitez", 26, "backend")
alan.hacerseElPiola()
alan.presentarse()

thomas = empleado("thomas", "gonzales", 26, "frontend")

thomas.presentarse()


persona1 = persona("alan", "benitez", 26)

