import time
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
from itertools import repeat


"""
Función: calcular_histograma
Entrada: El archivo de la imagen en formato .npy
Salida: El arreglo del histograma
"""
def calcular_histograma(filename_npy):
    # Cargamos la imagen .npy a un arreglo bidimensional
    imagen = np.load(filename_npy)  # La variable imagen viene a ser un arreglo bidimensional como cualquier otro

    #Información útil: Calcular las filas y columnas de la matriz (largo y ancho de la imagen)
    M = len(imagen)     # Número de filas
    N = len(imagen[0])  # Número de columnas

    # --- Escriba aquí su algoritmo para calcular el histograma [en lista] ---

    histograma_lista = [0]*256

    #print(imagen)

    for fila in range(M):
        for columna in range(N):
            elemento = imagen[fila][columna]
            histograma_lista[elemento] += 1

    return histograma_lista
    

"""
Función: graficar_histograma
Entradas:
- histograma_list: Su histograma que quiere graficar
- filename: Cadena de texto con el nombre del archivo para su gráfico que va a generar. Debe terminar en .png
- color: Cadena de texto con el color en inglés para su gráfico, 
Salida: Genera un gráfico de su histograma en formato .png
"""
def graficar_histograma(histograma_list, filename, color):
    plt.plot(range(0, len(histograma_list)), histograma_list, color=color)
    plt.savefig(filename, bbox_inches='tight')
    plt.close()

#############################################################################################

def plotear_histograma(nombre_de_archivo , tipo = 'serial' , color = 'g'):
    lista = calcular_histograma(f"{nombre_de_archivo}_x2.npy")
    graficar_histograma( lista , f"hist_{tipo}_{nombre_de_archivo}_x2.png" , color)
    print(f"Se generó la imagen hist_{tipo}_{nombre_de_archivo}_x2.png correctamente")

if __name__ == '__main__':

    archivos = ['goldhill' , 'hong kong' , 'lena' , 'stonehenge']

    # ---------------------- Parte a: Calculo del histograma en serial ----------------------

    inicio = time.perf_counter()

    for nombre in archivos:
        plotear_histograma(nombre)

    fin = time.perf_counter()

    tiempo_serie = fin-inicio

    print(f"Tiempo de ejecución en serie : {tiempo_serie} segundos")

    # ---------------------- Parte b: Calculo del histograma en paralelo ----------------------

    inicio = time.perf_counter()

    p = Pool(processes=4)
    resultado = p.starmap(plotear_histograma, zip(archivos, repeat('paralelo')))
    p.close()
    p.join()

    fin = time.perf_counter()

    tiempo_paralelo = fin - inicio

    print(f"Tiempo de ejecución en paralelo : {tiempo_paralelo} segundos")

    # ----------------
    
    SpeedUp = tiempo_serie / tiempo_paralelo
    print(f"SpeedUp = {SpeedUp} / El código en paralelo es más rápido que el código en serie")
