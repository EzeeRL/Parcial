# Funciones.py

def mostrar_votos(partidos, votos):
    total_votos = 0
    for i in range(len(partidos)):
        total_votos += sum(votos[i])
    
    for i in range(len(partidos)):
        votos_partido = sum(votos[i])
        porcentaje = (votos_partido * 100) / total_votos if total_votos > 0 else 0
        print("\nPartido:", partidos[i])
        print("CANTIDAD VOTOS TURNO 1:", votos[i][0])
        print("CANTIDAD VOTOS TURNO 2:", votos[i][1])
        print("CANTIDAD VOTOS TURNO 3:", votos[i][2])
        print("PORCENTAJE DE LOS VOTOS:", porcentaje, "%")

def partidos_menor_que(partidos, votos, porcentaje_limite):
    total_votos = sum([sum(v) for v in votos])
    encontrados = False
    for i in range(len(partidos)):
        porcentaje = (sum(votos[i]) * 100) / total_votos if total_votos > 0 else 0
        if porcentaje < porcentaje_limite:
            mostrar_votos([partidos[i]], [votos[i]])
            encontrados = True
    if not encontrados:
        print("No hay partidos con menos del", porcentaje_limite, "% de votos.")

def turno_mayor_participacion(votos):
    turnos = [0, 0, 0]
    for i in range(len(votos)):
        for j in range(3):
            turnos[j] += votos[i][j]
    max_votos = turnos[0]
    for val in turnos:
        if val > max_votos:
            max_votos = val
    print("Turnos con mayor participación:")
    for idx in range(3):
        if turnos[idx] == max_votos:
            print("Turno", idx+1, "con", turnos[idx], "votos.")

def promedio_general(votos):
    total_votos = sum([sum(v) for v in votos])
    promedio = total_votos / len(votos) if len(votos) > 0 else 0
    return promedio

def partidos_por_encima_del_promedio(partidos, votos):
    prom = promedio_general(votos)
    print("\nPromedio general de votos por partido:", prom)
    encontrados = False
    for i in range(len(partidos)):
        if sum(votos[i]) > prom:
            mostrar_votos([partidos[i]], [votos[i]])
            encontrados = True
    if not encontrados:
        print("Ningún partido supera el promedio.")

def buscar_partido(partidos, votos, nombre_busqueda):
    nombre_busqueda = nombre_busqueda.lower()
    encontrado = False
    for i in range(len(partidos)):
        if partidos[i].lower() == nombre_busqueda:
            mostrar_votos([partidos[i]], [votos[i]])
            encontrado = True
            break
    if not encontrado:
        print("Partido no encontrado.")

def ordenar_partidos_alfabeticamente(partidos):
    partidos_copy = []
    for i in range(len(partidos)):
        partidos_copy += [partidos[i]]

    # Ordenamiento burbuja (A-Z)
    n = len(partidos_copy)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if partidos_copy[j] > partidos_copy[j + 1]:
                # swap manual
                temp = partidos_copy[j]
                partidos_copy[j] = partidos_copy[j + 1]
                partidos_copy[j + 1] = temp

    print("\nPartidos ordenados alfabéticamente:")
    for partido in partidos_copy:
        print(partido)

