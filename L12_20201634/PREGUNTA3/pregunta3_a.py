import random
import time

if __name__ == '__main__':

    #Definciones iniciales
    valores_adentro = 0

    #Se define el número de muestras
    n = 10_000_000

    #Se hace el for loop para iterar cada muestra
    for i in range(n):

        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        distancia = (x*x + y*y)**0.5

        if (distancia<=1):
            valores_adentro += 1

    #Cálculo de PI
    resultado_pi = valores_adentro*4/n
    print(f"Valor PI calculado 3a = {resultado_pi}")
