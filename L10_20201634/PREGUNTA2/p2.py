#!/usr/bin/env python
from socket import AF_INET, SOCK_DGRAM
import datetime
import threading
import socket
import struct
import time

servidores_ntp = [
	"0.uk.pool.ntp.org",    # Londres(Reino Unido)
	"1.es.pool.ntp.org",    # Madrid (España)
	"0.us.pool.ntp.org",    # Nueva York(Estados Unidos)
	"0.hk.pool.ntp.org",    # Hong Kong
	"0.jp.pool.ntp.org"     # Tokyo(Japón)
]

"""
Función: get_ntp_time
Descripción: Imprime la  fecha-hora actual en un país determinado
Entrada: Cualquiera de las URLs definidas en la lista servidores_ntp
Salida: Retorna la fecha-hora(timestamp) en formato datetime.datetime, también la imprime
IMPORTANTE: NO modifique esta funcion 
"""

##################################################################################################

def get_ntp_time(host):
	timezone_dict = {'uk': ['UK', 0 * 3600], 'es': ['España', 1 * 3600],
	                 'hk': ['Hong Kong', 8 * 3600], 'jp': ['Japón', 9 * 3600],
	                 'us': ['Estados Unidos', -5*3600]}
	key = ''
	port = 123
	buf = 1024
	address = (host, port)
	msg = b'\x1b' + 47 * b'\0'

	# reference time (in seconds since 1900-01-01 00:00:00)
	TIME1970 = 2208988800  # 1970-01-01 00:00:00
	# connect to server
	client = socket.socket(AF_INET, SOCK_DGRAM)
	client.sendto(msg, address)
	msg, address = client.recvfrom(buf)
	t = struct.unpack("!12I", msg)[10]
	t -= TIME1970
	client.close()

	for each_key in timezone_dict:
		if each_key in host:
			key = each_key
			break
	print(f"Hora en {timezone_dict[key][0]}: {datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])}")
	return datetime.datetime.utcfromtimestamp(t + timezone_dict[key][1])

##################################################################################################

def funcion_iteracion():

	t = []

	for i in range(len(servidores_ntp)):
		dato = get_ntp_time(servidores_ntp[i])
		hora_str = dato.strftime("%H")
		hora_int = int(hora_str)
		t.append(hora_int)

	#print(t)

	rpta_indice = []

	for i in range(0,8+1):
		indice = 8-i
		
		for j in range(len(t)):
			if (indice == t[j]):
				rpta_indice.append(j)

	respuesta = max(rpta_indice)

	return respuesta

	#print("\nPaís y hora más próxima a abrir 08:00am es:")

	#return get_ntp_time(servidores_ntp[indice])

##################################################################################################

if __name__ == '__main__':

	#TIEMPO PARA DETERMINAR QUÉ PAÍS ABRE MÁS PRÓXIMO MEDIANTE EL CÁLCULO DEL ÍNDICE
	inicio = time.perf_counter()
	indice = funcion_iteracion()
	fin = time.perf_counter()

	#PROCESAMIENTO DEL ÍNDICE
	print("\nPaís (con su hora) más próximo a abrir 08:00am es:")
	get_ntp_time(servidores_ntp[indice])

	#MOSTRAR TIEMPO DE EJECUCIÓN
	print(f"Tiempo de ejecución: {fin-inicio} segundos")

	



	
	