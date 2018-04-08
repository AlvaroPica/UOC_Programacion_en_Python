import string
import math

# ################### EJERCICIO 1 ################## #

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
            masa = round(masa + masa_asociada_atomo, 2)
            # print identificador_atomo, cuantificador_atomo, masa_atomo, masa_asociada_atomo

        return masa


print calcula_masa_atomica('C13-H18-O2')
print calcula_masa_atomica('C8-H10-N4-O2')
print calcula_masa_atomica('C20-H25-N3-O')
print calcula_masa_atomica('C20-H10-O2-P2-S')

# ################### EJERCICIO 3 ################## #

# Completad las siguientes funciones matemmticas


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
    resultado = sum([a ** b * c for a, b, c in zip(vector_of_twos, power_index, multipliers)])
    return resultado


Lista_ejemplos = [101010101, 1111, 21311]
for ejemplo in Lista_ejemplos:
    print(binario_a_decimal(ejemplo))

# def fibonacci(n=100):
#     a, b = 0, 1
#     while a < n:
#         print a,b
#         a, b = b, a+b
#
# fibonacci(10)

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
lista_numeros = range(len(lista_abecedario))
diccionario_cesar_forward = dict(zip(lista_numeros, lista_abecedario))
diccionario_cesar_backwards = dict(zip(lista_abecedario, lista_numeros))


def cifrado_cesar(mensaje, desplazamiento):

    mensaje_original = mensaje.split()

    palabras_codificadas = []
    for palabras in mensaje_original:
        palabras = palabras.upper()
        letras_palabra = list(palabras)
        valores_palabra = [diccionario_cesar_backwards.get(x) for x in letras_palabra]
        valores_codificados = [x + desplazamiento for x in valores_palabra]
        letras_codificadas = [diccionario_cesar_forward.get(x) for x in valores_codificados]
        palabras_codificadas.append(''.join(letras_codificadas))
    mensaje_codificado = ' '.join(palabras_codificadas)

    print("El mensaje original es '%s' pero a las tropas les llegara como '%s' " % (mensaje,mensaje_codificado))


mensaje_normal = "Abanadonen el barco"
cifrado_cesar(mensaje_normal, 2)


# Las funciones range y xrange pueden utilizarse con la misma finalidad, pero su funcionamiento es distinto. Explicad en qué se diferencian y comentad para qué sirve la palabra
# # reservada yield. Poned un ejemplo de uso de range, xrange y otro de yield. (1 punto)

