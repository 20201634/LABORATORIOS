import time
from urllib.request import urlopen
from threading import Thread
from statistics import median

def lectura_rango(menor,mayor):

    for i in range(menor,mayor+1): 
        
        #FORMACIÓN DE URL:
        if (i<10):
            url = f"https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/0{i}.png"
            nombre = f"c_foto0{i}.png"
        else:
            url = f"https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/{i}.png"
            nombre = f"c_foto{i}.png"
        #print(url)

        #LECTURA DE URL:
        with urlopen(url) as page:
            image_data = page.read() #data como objeto binario

        #MOSTRAR IMAGEN
        with open(nombre,"wb") as f:
            f.write(image_data)

def main():
    t1 = Thread(target=lectura_rango,args=(1,10))
    t2 = Thread(target=lectura_rango,args=(11,20))
    t3 = Thread(target=lectura_rango,args=(21,29))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':

    t = []

    for _ in range(5):
        inicio = time.perf_counter()
        main()
        fin = time.perf_counter()
        t.append(fin-inicio)
    
    #print(t)
    print(f"Tiempo de ejecución 3 hilos: {median(t)} segundos")

#Comentarios:

#Con respecto al tiempo de ejecución en "b" se obtuvo un tiempo mayor de ejecución.
#Esto se debe a que para solucion_b.py se usaron 29 hilos (1 por cada imagen), lo cual
#va a acelerar el proceso significativamente con respecto a usar 3 hilos para dividir las
#29 operaciones en 3 paquetes y realizar dichos 3 paquetes de manera concurrente.

        

   