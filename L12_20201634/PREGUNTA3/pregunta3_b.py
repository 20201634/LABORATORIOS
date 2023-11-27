import random
import time
from multiprocessing import Pool, Process

#########################################################################################################

def valores_adentro_area(rango_x,rango_y,muestras): # Ej: rango_x = [0,1] , rango_y = [0,1]

    resultado = 0

    for i in range(muestras):
        x = random.uniform(rango_x[0] , rango_x[1])
        y = random.uniform(rango_y[0] , rango_y[1])
        distancia = (x*x + y*y)**0.5
        if (distancia<=1):
            resultado += 1

    return resultado




#########################################################################################################

if __name__ == '__main__':

    #Se inicializa
    valores_adentro = 0

    #Se define el número de muestras
    n = 10_000_000

    #Se realizan 4 procesos
    args = [ [ [0,1] , [0,1] , n//4] , [ [0,1] , [-1,0] , n//4] , [ [-1,0] , [0,1] , n//4] , [ [-1,0] ,[-1,0] , n//4]]
    p = Pool(processes=4)
    resultado = p.starmap( valores_adentro_area , args)
    p.close()
    p.join()

    #print(resultado)

    #Cálculo de valores_adentro
    for elemento in resultado:
        valores_adentro += elemento

    #Cálculo de PI
    resultado_pi = valores_adentro*4/n
    print(f"Valor PI calculado 3b = {resultado_pi}")