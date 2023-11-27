import time
from werkzeug.security import check_password_hash #INSTALE ESTA LIBERIA, tipee en su terminal: pip install Werkzeug
from multiprocessing import Pool, Process

"""
Esta es la contraseña que usted tiene que adivinar. Está encriptada para que no pueda saber cuál es la respuesta correcta a priori.
Lo que tiene que hacer es generar combinaciones de 3 letras y llamar a la función comparar_con_password_correcto(línea 20 de la plantilla)
"""
contrasena_correcta = 'pbkdf2:sha256:260000$rTY0haIFRzP8wDDk$57d9f180198cecb45120b772c1317b561f390d677f3f76e36e0d02ac269ad224'


# Arreglo con las letras del abecedario. Puede serle de ayuda, no es obligatorio que lo use
abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vocales = ['a','e','i','o','u']

"""
Función que sirve para comparar su palabra(cadena de 3 caracteres) con la contraseña correcta.
Entrada: Su cadena de 3 caracteres
Salida: True(verdadero) si es que coincide con la contraseña correcta, caso contrario retorna False(falso)
"""
def comparar_con_password_correcto(palabra):
	return check_password_hash(contrasena_correcta, palabra)

################################################################

def password_sync() -> str:

	palabra_lista = list()
	resultado = 0

	for a in range(len(vocales)):

		for b in range(len(vocales)):

			for c in range(len(abecedario)):

				palabra_lista.append(vocales[a]) #Agregar la primera vocal
				palabra_lista.append(vocales[b]) #Agregar la segunda vocal
				palabra_lista.append(abecedario[c]) #Agregar la tercera letra

				# --- Trabajar con la lista que ya tiene las 3 letras ---
				#print(palabra_lista) #COMENTAR - palabra en lista

				# Transformar lista a str
				palabra_str = ''.join(palabra_lista)
				#print(palabra_str) #COMENTAR - palabra en str

				# Verificar si palabra_str es la contraseña
				if ( comparar_con_password_correcto(palabra_str) == True ):
					#print(f"Se encontró la contraseña: {palabra_str}")
					resultado = palabra_str
				
				# --- Resetear la lista y probar otra ---
				palabra_lista = list()

	return resultado



if __name__ == "__main__":
	
	inicio = time.perf_counter()
	password = password_sync()
	fin = time.perf_counter()

	print(f"Contraseña : {password} / Tiempo de ejecución : {fin-inicio} segundos")
	
	pass
