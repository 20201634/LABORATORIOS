import time
from urllib.request import urlopen
from threading import Thread
from statistics import median

def lectura_i(i):
        
    #FORMACIÓN DE URL:
    if (i<10):
        url = f"https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/0{i}.png"
        nombre = f"b_foto0{i}.png"
    else:
        url = f"https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/{i}.png"
        nombre = f"b_foto{i}.png"
    #print(url)

    #LECTURA DE URL:
    with urlopen(url) as page:
        image_data = page.read() #data como objeto binario

    #MOSTRAR IMAGEN
    with open(nombre,"wb") as f:
        f.write(image_data)

def main():

    for i in range(1,30):
        t = Thread(target=lectura_i,args=(i,))
        t.start()

if __name__ == '__main__':

    t = []

    for _ in range(5):
        inicio = time.perf_counter()
        main()
        fin = time.perf_counter()
        t.append(fin-inicio)
    
    #print(t)
    print(f"Tiempo de ejecución multihilo: {median(t)} segundos")

#Comentarios:

#Ahora que se está usando multihilo se observa que el tiempo de ejecución es
#mucho más rápido. Esto se debe a que para solucion_a.py se realiza la lectura e impresión de
#las imágenes de manera secuencial una por una hasta llegar a las 29 imágenes, mientras que
#para solucion_b.py se usó multihilo y las 29 operaciones se hacen de manera concurrente.

        

   