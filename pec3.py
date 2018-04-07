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

