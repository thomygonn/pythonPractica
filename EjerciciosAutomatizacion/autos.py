def concesionaria():
    Marcas = {'Ford':100000,'Chevrolet':120000,'Fiat':80000}
    Puertas = {'2':50000,'4':65000, '5':78000}
    Color = {'blanco':10000, 'azul':20000, 'negro':30000}
    nombre_apellido = input('Ingrese su nombre y apellido ')
    marcas = input('Ingrese la marca del auto entre Ford, Chevrolet y Fiat ')
    puertas = input('Ingrese el número de puertas entre 2, 4 o 5 ')
    color = input('Que color preferis ? Tenemos blanco, negro y azul ')

    if marcas == 'Ford' or 'ford':
        return Marcas.keys(0)
    if marcas == 'chevrolet' or 'Chevrolet':
        return Marcas.keys(1)
    if marcas == 'fiat' or 'Fiat':
        return Marcas.keys(2)
    
    if puertas == '2':
        return Puertas.keys(0)
    if puertas == '4':
        return Puertas.keys(1)
    if puertas == '5':
        return Puertas.keys(2)
    
    if color == 'blanco' or 'Blanco':
        return Color.keys(0)
    if color == 'azul' or 'Azul':
        return Color.keys(1)
    if color == 'negro' or 'Negro':
        return Color.keys(2)
    
    if marcas == 'Ford' and 'puertas' == '2' and color == 'blanco':
        print(f' El precio total es', Marcas.keys(0)+ Puertas.keys()+ Color.keys(0))
    elif marcas == 'Chevrolet' and 'puertas' == '4' and color == 'negro':
        print(f'El precio total es',Marcas.keys(1)+ Puertas.keys(1)+ Color.keys(2))   
    elif marcas == 'Ford' and 'puertas' == '5' and color == 'azul':
        print(f'El precio total es',Marcas.keys(2)+ Puertas.keys(2)+ Color.keys(1))   
    else:
        print('Ingrese datos validos')

#concesionaria()