import random
import time
import asyncio
import aiofiles


async def genera_labs():
    codigo_inicial = 20230001
    async with aiofiles.open("notas_labs_async.csv", "w+", encoding="utf-8") as f:
        
        cabecera = "codigo,"
        cabecera += ",".join([f"lab_{i}" for i in range(1, 15)])
        cabecera += "\n"
        await f.write(cabecera)

        for i in range(200):
            linea = f"{codigo_inicial + i},"
            linea += ",".join([f"{random.randint(0, 20)}" for i in range(1, 15)])
            linea += "\n"
            await f.write(linea)


async def genera_parcial():
    codigo_inicial = 20230001
    async with aiofiles.open("notas_parcial_async.csv", "w+", encoding = "utf-8") as f:
        cabecera = "codigo,parcial\n"
        await f.write(cabecera)

        for i in range(200):
            linea = f"{codigo_inicial + i},{random.randint(0, 20)}\n"
            await f.write(linea)


async def genera_final():
    codigo_inicial = 20230001
    async with aiofiles.open("notas_final_async.csv", "w+", encoding = "utf-8") as f:
        cabecera = "codigo,final\n"
        await f.write(cabecera)

        for i in range(200):
            linea = f"{codigo_inicial + i},{random.randint(0, 20)}\n"
            await f.write(linea)


async def main():

    await asyncio.gather(genera_labs(),genera_parcial(),genera_final())

if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    print(f"Tiempo de ejecución async: {fin - inicio} segundos")

# COMENTARIOS :

# Se esperaría que el código asíncrono sea más rápido que el síncrono ya que
# en vez de estar enviando una petición (llamado de la función) y esperar a que termine
# se envían varias peticiones de manera concurrente y esto tardará menos ya que no espera
# al resultado de dicha función (o a que termine) en dicho momento.
# Sin embargo, debido al uso de la librería aiofiles modifica el tiempo esperado de ejecución.
# La E/S de archivos .csv no se puede hacer de manera asíncrona por sí sola, por lo que
# aiofiles ayuda a que se generen versiones asíncronas de archivos que permiten la 
# delegación de operaciones a un grupo de subprocesos independiente. Esta acción a pesar de
# aligerar el tiempo igual consume una cantidad adicional de tiempo por el procesamiento que
# está involucrado en hacer todo ese artificio informático para usar archivos de manera asíncrona.
# Por ello en este ejemplo la versión síncrona es más rápida que la versión asíncrona.
