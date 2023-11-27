# CÓDIGO A - lectura de players.csv
# este código y sus funciones se reutilizarán en los siguientes códigos

if __name__ == "__main__":
    
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

    print(lista_nombres)
    print(lista_rating)

