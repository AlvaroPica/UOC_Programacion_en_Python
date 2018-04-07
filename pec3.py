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

# Masas atomicas

masas = {'H': 1.007825, 'C': 12.01, 'O': 15.9994, 'N': 14.0067, 'S': 31.972071, 'P': 30.973762}

def calcula_masa_atomica(molecula):
    """
    Calcula la masa atomica de una molecula
    """
    masa = 0.0

    atomos_molecula = molecula.split("-")  # type: object

    for ii in atomos_molecula:
        identificador_atomo = list(ii)[0]
        cuantificador_atomo = ii[1:]
        if cuantificador_atomo == '':
            cuantificador_atomo = "1"
        cuantificador_atomo = int(cuantificador_atomo)
        masa_atomo = masas[identificador_atomo]
        masa_asociada_atomo = cuantificador_atomo * masa_atomo
        masa = masa + masa_asociada_atomo
        # print identificador_atomo, cuantificador_atomo, masa_atomo, masa_asociada_atomo

    return masa


print calcula_masa_atomica('C13-H18-O2')
print calcula_masa_atomica('C8-H10-N4-O2')
print calcula_masa_atomica('C20-H25-N3-O')
print calcula_masa_atomica('C20-H10-O2-P2-S')
