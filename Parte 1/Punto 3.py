def eliminar_vocales_repetidas(cadena):
    nueva_cadena = ""
    vocales = "aeiou"
    usadas = []

    for caracter in cadena:
        codigo = ord(caracter)
        if 65 <= codigo <= 90:
            minuscula = chr(codigo + 32)
        else:
            minuscula = chr(codigo)

        if minuscula in vocales:
            if minuscula not in usadas:
                usadas.append(minuscula)
                nueva_cadena += caracter
        else:
            nueva_cadena += caracter

    return nueva_cadena


texto = input("Ingrese una cadena de texto: ")
resultado = eliminar_vocales_repetidas(texto)
print("Resultado:", resultado)
