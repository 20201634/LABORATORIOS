import time
from urllib.request import urlopen
from statistics import median

def lectura_rango(menor,mayor):

    for i in range(menor,mayor+1): 
        
        #FORMACIÓN DE URL:
        if (i<10):
            url = f"https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/0{i}.png"
            nombre = f"a_foto0{i}.png"
        else:
            url = f"https://raw.githubusercontent.com/SebastianMerino/Threading/main/images/{i}.png"
            nombre = f"a_foto{i}.png"
        #print(url)

        #LECTURA DE URL:
        with urlopen(url) as page:
            image_data = page.read() #data como objeto binario

        #MOSTRAR IMAGEN
        with open(nombre,"wb") as f:
            f.write(image_data)

def main():
    lectura_rango(1,29)

if __name__ == '__main__':

    t = []

    for _ in range(5):
        inicio = time.perf_counter()
        main()
        fin = time.perf_counter()
        t.append(fin-inicio)
    
    #print(t)
    print(f"Tiempo de ejecución normal: {median(t)} segundos")

        

   