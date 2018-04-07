# ## Ejercicio 1 ## #

# Completad el ccdigo necesario para calcular el numero de palabras y de espacios de un texto.
# El numero de espacios no tiene que ser necesariamente funcion del numero de
# palabras. (1 punto)

def contar_palabras_y_espacios(texto):
    num_palabras = 0
    num_espacios = 0

    num_espacios = texto.count(" ")
    string_split = texto.split(" ")

    if string_split[-1] == "":
        string_split = string_split[:-1]

    num_espacios = len(string_split)

    print("El numero de palabras es %d" % num_espacios)
    print("El numero de espacios es %d" % num_espacios)

    return string_split


texto = "Hola 1 2 3+1 n "
string_split = contar_palabras_y_espacios(texto)

# ## Ejercicio 2 ## #

# Masas atomicas

masas = {'H': 1.007825, 'C': 12.01, 'O': 15.9994, 'N': 14.0067, 'S': 31.972071, 'P': 30.973762}


def calcula_masa_atomica(molecula):
        """
        Calcula la masa atomica de una molecula
        """
        masa = 0.0

        atomos_molecula = molecula.split("-")

        for ii in atomos_molecula:
            identificador_atomo = list(ii)[0]
            cuantificador_atomo = ii[1:]
            if cuantificador_atomo == '':
                cuantificador_atomo = "1"
            cuantificador_atomo = float(cuantificador_atomo)
            masa_atomo = masas[identificador_atomo]
            masa_asociada_atomo = cuantificador_atomo * masa_atomo
            masa = round(masa + masa_asociada_atomo, 2)
            # print identificador_atomo, cuantificador_atomo, masa_atomo, masa_asociada_atomo

        return masa


print calcula_masa_atomica('C13-H18-O2')
print calcula_masa_atomica('C8-H10-N4-O2')
print calcula_masa_atomica('C20-H25-N3-O')
print calcula_masa_atomica('C20-H10-O2-P2-S')

# ## Ejercicio 3 ## #

# Completad las siguientes funciones matemmticas

import math


def area_circulo(radio):

    area = round(math.pi * radio ** 2, 2)

    return area


print("El area de un circulo de radio 3 cm es de %.2f cm2" % area_circulo(3))


def longitud_circulo(radio):

    longitud = 2 * math.pi * radio

    return longitud


print("La longitud de circulo de radio 3 cm es de %.2f cm" % longitud_circulo(3))


def hipotenusa(cateto1, cateto2):

    hipotenusa_triangulo = math.sqrt((math.pow(cateto1, 2) + math.pow(cateto2, 2)))

    return hipotenusa_triangulo


print("La hipotenua de un triangulo de catetos de 3 y 5 cm respectivamente mide %.2f cm" % hipotenusa(3, 5))


def area_cuadrado(lado):

    area = lado * lado

    return area  # puedo llamar a una variable local como otras variables locales dentro de otros procedimientos?"


def volumen_esfera(radio):

    volumen = math.pi * math.pow(radio, 3)

    return volumen


print("El volumen de una esfera de 3 cm de radio es de %.2f cm3" % volumen_esfera(3))


def volumen_cubo(lado):

    volumen = math.pow(lado, 3)

    return volumen


print("El volumen de una cubo de 3 cm de arista es de %.2f cm3" % volumen_cubo(3))

# Escribid aqui algunos ejemplos utilizando estas funciones, por ejemplo:
# print 'El volumen del cubo de lado 3.5 es %f' % volumen_cubo(3.5)

# ## EJERCICIO 4 ### #

# El siguiente ejercicio consiste en pasar un numero en base 2 (binario, 0/1) a base 10 (decimal).
# Dado un string que representa un numero en binario, por ejemplo, 1011, devolved el nUmero natural
# correspondiente, en este caso, 11. (1.5 puntos)


def binario_a_decimal(numero_a_convertir):
    numero_a_convertir = str(numero_a_convertir)
    numero_a_convertir = list(numero_a_convertir)

    for ii in numero_a_convertir:
        if ii not in ["0", "1"]:
            print("El numero no es binario")
            exit
    print("Procedemos a la Conversion del numero binario:")

    print(numero_a_convertir)
    print(len(numero_a_convertir))

    power_index = []
    for ii in range(0, (len(numero_a_convertir))):
        print type(int(ii))
        power_index.append([ii])
    print power_index, type(power_index)

    multipliers = []
    for jj in numero_a_convertir:
        print type(int(jj))
        multipliers.append([int(jj)])
    print multipliers, type(multipliers)

    return numero_a_convertir

    # vector_of_twos

numero = binario_a_decimal(1101)

