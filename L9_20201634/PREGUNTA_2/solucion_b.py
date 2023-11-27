# CÓDIGO B (ASÍNCRONO) - fase de rondas

import time
import aiofiles
import asyncio


def funcion_archivo():
    lista_nombres = []
    lista_rating = []
    
    #LECTURA DE DATOS
    with open("players.csv", "r", encoding = "utf-8") as f:
        contenido = f.readlines()

    #OBTENCIÓN DE NOMBRE Y RATING
        
    for x in range(1,6+1):
        flag = 0
        exp = 3
        nivel = 0
        nombre = ""

        for i in range(len(contenido[x])-1):

            if flag == 1:
                nivel += int(contenido[x][i])*pow(10,exp)
                #print(nivel)
                exp -= 1

            if contenido[x][i] == ";":
                flag = 1

            if flag == 0:
                nombre += contenido[x][i]

        #print(nivel)
        #print(nombre)
        lista_nombres.append(nombre)
        lista_rating.append(nivel)

    #print(lista_nombres)
    #print(lista_rating)
    return lista_nombres , lista_rating

##################

nombres_rating = funcion_archivo()
puntaje = [0,0,0,0,0,0]

##################
async def dia1():
    
    # Levon vs Magnus
    p1 = 3
    p2 = 0
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

    #Boris vs Alexander
    p1 = 4
    p2 = 5
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

    #Peter vs Vladimir
    p1 = 2
    p2 = 1
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

async def dia2():

    # M vs V
    p1 = 0
    p2 = 1
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

    # A vs P
    p1 = 5
    p2 = 2
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

    # L vs B
    p1 = 3
    p2 = 4
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

async def dia3():

    # B vs M
    p1 = 4
    p2 = 0
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

    # P vs L
    p1 = 2
    p2 = 3
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

    # V vs A
    p1 = 1
    p2 = 5
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

async def dia4():

    # M vs A
    p1 = 0
    p2 = 5
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

    # L vs V
    p1 = 3
    p2 = 1
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

    # B vs P
    p1 = 4
    p2 = 2
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

async def dia5():
    
    # P vs M 
    p1 = 2
    p2 = 0
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

    # V vs B
    p1 = 1
    p2 = 4
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

    # A vs L 
    p1 = 5
    p2 = 3
    if nombres_rating[1][p1] > nombres_rating[1][p2]:
        puntaje[p1] += 1
    else:
        puntaje[p2] += 1
    await asyncio.sleep(0.15)

async def fase_rondas_sync():

    #DESARROLLO DE RONDAS
    await asyncio.gather(dia1(),dia2(),dia3(),dia4(),dia5())

    #OBTENER EL MÁXIMO VALOR DE ÍNDICE en a
    for i in range(0,6):
        if (max(puntaje) == puntaje[i]):
            a = i

    return nombres_rating[0][a]
    


if __name__ == "__main__":

    inicio = time.perf_counter()
    rpta = asyncio.run(fase_rondas_sync())
    fin = time.perf_counter()
    print(f"Ganador fase rondas = {rpta} / Tiempo (async) = {fin-inicio} segundos")




    

    
    
    
    
