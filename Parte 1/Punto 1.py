# Ezequiel Damián Ramos Lencina. Div 115
# ====== PUNTO 1 ======
import random

arreglo = [None] * 10

print("=== CARGA ALEATORIA DE UN ARREGLO DE FLOTANTES ===\n")

def es_numero_real(cadena):
    tiene_punto = False
    if len(cadena) == 0:
        return False

    for i in range(len(cadena)):
        c = cadena[i]
        if c == "-":
            if i != 0:
                return False
        elif c == ".":
            if tiene_punto:
                return False
            tiene_punto = True
        elif ord(c) < 48 or ord(c) > 57:
            return False
    return True

# Carga de 10 números
for i in range(10):
    while True:
        numero_str = input(f"Ingrese un número real ({i+1}/10): ")
        if es_numero_real(numero_str):
            numero = float(numero_str)
            break
        else:
            print("Error: Debe ingresar un número válido (solo dígitos y punto).")

    # Asignación aleatoria
    while True:
        pos = random.randint(0, 9)
        if arreglo[pos] is None:
            arreglo[pos] = numero
            break

# Mostrar el resultado
print("\nArreglo cargado en posiciones aleatorias:\n")
for i, valor in enumerate(arreglo):
    print(f"Posición {i}: {valor}")
