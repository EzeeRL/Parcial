# Inputs.py

def ingresar_nombre_partido(posicion):
    valido = False
    while not valido:
        nombre = input(f"Ingrese el nombre del partido {posicion}: ")
        
        if len(nombre) >= 3:
            solo_letras = True
            for c in nombre:
                if not (c.isalpha() or c == " "):
                    solo_letras = False
            if solo_letras:
                valido = True
                return nombre
            else:
                print("❌ Nombre inválido. Solo se permiten letras y espacios.")
        else:
            print("❌ Nombre demasiado corto. Debe tener al menos 3 caracteres.")


def ingresar_votos_partido(partido, turno):
    valido = False
    while not valido:
        texto = input(f"Ingrese los votos para '{partido}' en Turno {turno}: ")
        
        es_numero = True
        for c in texto:
            if not c.isdigit():
                es_numero = False

        if es_numero and texto != "":
            votos = int(texto)
            if votos >= 0:
                valido = True
                return votos
            else:
                print("❌ No se permiten valores negativos.")
        else:
            print("❌ Ingrese un número entero válido.")
