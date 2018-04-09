import string
import math

# ################### EJERCICIO 1 ################## #

# Completad el ccdigo necesario para calcular el numero de palabras y de espacios de un texto.
# El numero de espacios no tiene que ser necesariamente funcion del numero de
# palabras. (1 punto)


def contar_palabras_y_espacios(texto_a_evaluar):

    num_espacios = texto_a_evaluar.count(" ")
    string_split = texto_a_evaluar.split(" ")

    if string_split[-1] == "":
        string_split = string_split[:-1]

    num_palabras = len(string_split)

    return num_palabras, num_espacios


texto = "Orbiting Earth in the spaceship, I saw how beautiful our planet is. \
            People, let us preserve and increase this beauty, not destroy it!"

num_palabras, num_espacios = contar_palabras_y_espacios(texto)
print "El numero de palabras es de %d" % num_palabras
print "El numero de espacios es de %d" % num_espacios

# ################### EJERCICIO 2 ###################

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
            masa = masa + masa_asociada_atomo
            # print identificador_atomo, cuantificador_atomo, masa_atomo, masa_asociada_atomo

        return masa


print('La masa es %.2f' % calcula_masa_atomica('C13-H18-O2'))
print calcula_masa_atomica('C8-H10-N4-O2')
print calcula_masa_atomica('C20-H25-N3-O')
print calcula_masa_atomica('C20-H10-O2-P2-S')

# ################### EJERCICIO 3 ################## #

# Completad las siguientes funciones matemmticas


def area_circulo(radio):

    area = math.pi * radio ** 2

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

# ################### EJERCICIO 4 ################## #

# El siguiente ejercicio consiste en pasar un numero en base 2 (binario, 0/1) a base 10 (decimal).
# Dado un string que representa un numero en binario, por ejemplo, 1011, devolved el nUmero natural
# correspondiente, en este caso, 11. (1.5 puntos)


def binario_a_decimal(numero_a_convertir):

    numero_a_convertir = str(numero_a_convertir)
    numero_a_convertir = list(numero_a_convertir)
    for ii in numero_a_convertir:
        if ii not in ["0", "1"]:
            print("El numero %s no es binario" % ''.join(numero_a_convertir))
            return "Introduzca un numero binario"
    print("El numero decimal correspondiente al numero binario %s es:" % ''.join(numero_a_convertir))
    vector_of_twos = []
    power_index = []
    multipliers = []
    for ii in range(0, (len(numero_a_convertir))):
        vector_of_twos.append(2)
        power_index.insert(0, ii)
        multipliers.append(int(numero_a_convertir[ii]))
    resultado = sum([(a ** b) * c for a, b, c in zip(vector_of_twos, power_index, multipliers)])

    return resultado


Lista_ejemplos = [101010101, 1111, 21311]
for ejemplo in Lista_ejemplos:
    print(binario_a_decimal(ejemplo))

# ################### EJERCICIO 5 ################## #
# Uno de los algoritmos mas basicos en criptografia es el cifrado Cesar (https://es.wikipedia.org/wiki/Cifrado_
# C%C3%A9sar), que fue utilizado por Julio Cesar para comunicarse # con sus generales, y que consiste en dado un texto,
#  por cada una de las letras del texto, aniadirle un desplazamiento para conseguir una nueva letra diferente de la
#  original. # Comprenderemos rapidamente su mecanismo mediante un ejemplo: # Si asignamos el numero 1 a la primera
# letra del abecedario, A, 2 a la siguiente, B, etc., imaginad que tenemos el siguiente mensaje:
# ABC
# 123
# Si aplicamos un desplazamiento de 3, buscaremos cual es la letra en el abecedario que se corresponde:
# DEF
# 456
# ABC se ha convertido en DEF porque hemos sumado un desplazamiento de 3. Tambien podriamos aplicar otros tipos
# de desplazamiento como los negativos. Por ejemplo, para
# el desplazamiento -1 y el mensaje original ABC tendriamos un mensaje cifrado de: ZAB.
# Escribid una funcion que dado un mensaje original y un desplazamiento, calcule y devuelva el mensaje cifrado.
# 1.5 puntos

lista_abecedario = list(string.ascii_uppercase)
num_letras_abecedario = len(lista_abecedario)
lista_numeros = range(num_letras_abecedario)
diccionario_cesar_forward = dict(zip(lista_numeros, lista_abecedario))
diccionario_cesar_backwards = dict(zip(lista_abecedario, lista_numeros))


def cifrado_cesar(mensaje, desplazamiento):

    mensaje = mensaje.split()

    palabras_codificadas = []
    for palabra in mensaje:
        palabra = palabra.upper()
        letras_palabra = list(palabra)
        valores_palabra = [diccionario_cesar_backwards[x] for x in letras_palabra]
        valores_codificados = [x + desplazamiento for x in valores_palabra]
        letras_codificadas = [diccionario_cesar_forward[x % num_letras_abecedario] for x in valores_codificados]
        palabras_codificadas.append(''.join(letras_codificadas))
    mensaje_cifrado = ' '.join(palabras_codificadas)
    return mensaje_cifrado


mensaje = "Abanadonen el barco"
print("El mensaje original es '%s' pero a las tropas les llegara como '%s' " % (mensaje, cifrado_cesar(mensaje, 26)))



# Las funciones range y xrange pueden utilizarse con la misma finalidad, pero su funcionamiento es distinto.
# Explicad en que se diferencian y comentad para qu? sirve la palabra
# # reservada yield. Poned un ejemplo de uso de range, xrange y otro de yield. (1 punto)

