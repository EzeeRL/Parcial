# ====== PUNTO 2 ======
# Ezequiel Damián Ramos Lencina

def factorial(n):
    if n < 0:
        print("Error: no existe el factorial de un número negativo.")
        return None

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("=== CÁLCULO DEL FACTORIAL DE UN NÚMERO ===\n")

numero = input("Ingrese un número entero positivo: ")

if numero.isdigit():
    numero = int(numero)
    resultado = factorial(numero)
    if resultado is not None:
        print(f"El factorial de {numero} es: {resultado}")
else:
    print("Error: Debe ingresar un número entero válido.")
