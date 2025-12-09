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