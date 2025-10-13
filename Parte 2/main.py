# Main.py
import Inputs
import Funciones

def menu():
    partidos = [None] * 5
    votos = [[0, 0, 0] for _ in range(5)]
    nombres_cargados = False
    votos_cargados = False

    while True:
        print("\n=== MENÚ DE ELECCIONES UTN FRA ===")
        print("1. Cargar nombres de partidos")
        print("2. Cargar votos de los partidos")
        print("3. Mostrar votos")
        print("4. Partidos con menos del 5% de votos")
        print("5. Partidos con menos del 10% de votos")
        print("6. Turno con mayor participación")
        print("7. Partidos por encima del promedio")
        print("8. Buscar partido por nombre")
        print("9. Ordenar partidos alfabéticamente")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            for i in range(5):
                partidos[i] = Inputs.ingresar_nombre_partido(i + 1)
            print("✅ Nombres cargados correctamente.")
            nombres_cargados = True

        elif opcion == "2":
            if not nombres_cargados:
                print("❌ Primero debe cargar los nombres de los partidos.")
                continue

            for i in range(5):
                for j in range(3):
                    votos[i][j] = Inputs.ingresar_votos_partido(partidos[i], j + 1)

            print("✅ Votos cargados correctamente.")
            votos_cargados = True

        elif opcion == "3":
            if not votos_cargados:
                print("❌ Primero debe cargar los votos de los partidos.")
                continue
            Funciones.mostrar_votos(partidos, votos)

        elif opcion == "4":
            if not votos_cargados:
                print("❌ Primero debe cargar los votos de los partidos.")
                continue
            Funciones.partidos_menor_que(partidos, votos, 5)

        elif opcion == "5":
            if not votos_cargados:
                print("❌ Primero debe cargar los votos de los partidos.")
                continue
            Funciones.partidos_menor_que(partidos, votos, 10)

        elif opcion == "6":
            if not votos_cargados:
                print("❌ Primero debe cargar los votos de los partidos.")
                continue
            Funciones.turno_mayor_participacion(votos)

        elif opcion == "7":
            if not votos_cargados:
                print("❌ Primero debe cargar los votos de los partidos.")
                continue
            Funciones.partidos_por_encima_del_promedio(partidos, votos)

        elif opcion == "8":
            if not votos_cargados:
                print("❌ Primero debe cargar los votos de los partidos.")
                continue
            nombre_busqueda = input("Ingrese el nombre del partido a buscar: ")
            Funciones.buscar_partido(partidos, votos, nombre_busqueda)

        elif opcion == "9":
            if not nombres_cargados:
                print("❌ Primero debe cargar los nombres de los partidos.")
                continue
            Funciones.ordenar_partidos_alfabeticamente(partidos)

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("❌ Opción inválida. Ingrese un número del 0 al 9.")


if __name__ == "__main__":
    menu()
