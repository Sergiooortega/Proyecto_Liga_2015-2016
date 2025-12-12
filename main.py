import csv

def leerPartidos():
    partidos= []

    with open("liga.csv",newline="",encoding="utf-8") as fichero:
        lector = csv.reader(fichero)
        next(lector)

        for fila in lector:
            goles_local,goles_visitante = map(int, fila[3].split('-'))
            partido ={
                "fecha":fila[0],
                "local":fila[1],
                "visitante":fila[2],
                "goles_local":goles_local,
                "goles_visitante":goles_visitante
            }
            partidos.append(partido)
    return partidos 


def equipos(datosLiga):

    conjunto_equipos = set()

    for partido in datosLiga:
        conjunto_equipos.add(partido['local'])
        conjunto_equipos.add(partido['visitante'])

    return conjunto_equipos

def infoEquipos(datosliga,equipos):
    info = {equipo: [0, 0, 0] for equipo in equipos}

    for partido in datosliga:
        local = partido["local"]
        visitante = partido["visitante"]
        golLocal = partido["goles_local"]
        golVisi = partido["goles_visitante"]

        if golLocal == golVisi:
            info[local][1] += 1
            info[visitante][1] += 1

        elif golLocal > golVisi:
            info[local][0] += 1
            info[visitante][2] += 1

        else:
            info[visitante][0] += 1
            info[local][2] += 1

    lista_info = []
    for equipo in equipos:
        ganado, empa, perdido = info[equipo]
        puntos = ganado * 3 + empa
        lista_info.append((equipo, ganado, empa, perdido, puntos))

    return lista_info

def quienGana(resultado):
    golLocal, golVisi = map(int, resultado.split("-"))

    if golLocal == golVisi:
        return 0
    elif golLocal > golVisi:
        return 1
    else:
        return -1

def puntos(info):
    ganado, empa, perdido = info
    return ganado * 3 + empa


def clasificacion(datos):
    for i in range(len(datos)):
        for j in range(i+1, len(datos)):
            if datos[j][4] > datos[i][4]:
                datos[i], datos[j] = datos[j], datos[i]
            elif datos[j][4] == datos[i][4] and datos[j][0] < datos[i][0]:
                datos[i], datos[j] = datos[j], datos[i]
    return datos

