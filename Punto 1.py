# Ejercicio 1 - Carga manual de un arreglo unidimensional de flotantes
# sin usar append(), insert(), ni métodos de listas.

def cargar_arreglo():
    TAM = 10
    arreglo = [0] * TAM  # inicializo la lista con 10 posiciones vacías

    print("=== CARGA DE 10 NÚMEROS REALES ===")
    
    for i in range(TAM):
        valido = False
        while not valido:
            dato = input(f"Ingrese el número real {i+1}: ")
            try:
                numero = float(dato)  # intento convertir a flotante
                arreglo[i] = numero   # asigno directamente por índice
                valido = True
            except ValueError:
                print("❌ Error: debe ingresar un número real (use punto para decimales).")
    
    print("\n✅ Arreglo cargado correctamente:")
    print(arreglo)

    return arreglo


# Ejecución del programa
cargar_arreglo()
