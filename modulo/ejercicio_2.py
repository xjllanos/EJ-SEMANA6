# EJERCICIO 2 
    #ORDENAR LAS LISTAS DE LISTA1 Y LISTA2 EN PARALELO, BASANDOSE EN LISTA1 
    #PERO SI HAY DATOS IGUALES FIJARSE EN LISTA2
    #RECIBE DOS LISTAS: MATERIAS Y PUNTOS 
    #DEVUELVE LAS DOS LISTAS ORDENADAS
    
    #USO BUBBLE SORT 

def ordenar_x_iguales(matriz:list) -> list: 

    lista1 = matriz[0]
    lista2 = matriz[1]
    
    if type(lista1)!= list or type(lista2) != list: 
        print("El paramentro de la funcion debe ser una lista")
        return None 
    
    n = len(lista1) #EL VALOR DE n MIDO LA LONGITUD DE LISTA

    if n != len(lista2):
        print("listas1 y lista2 deben tener la misma longitud")
        return None
    

    for i in range(n):
        intercambio = False 

        for j in range(0, n - i - 1):
            if matriz[0][j] > matriz[0][j+1]:
                intercambio = True 
                #INTERCAMBIAR LISTA1
                menor = lista1[j+1]
                matriz[0][j+1] = matriz[0][j]
                matriz[0][j] = menor
                #INTERCAMBIAR LISTA2 PARA QUE ESTEN ENLAZADAS
                menor2 = matriz[1][j+1]
                matriz[1][j+1] = matriz[1][j]
                matriz[1][j] = menor2
            
            elif matriz[0][j] == matriz[0][j+1]: #VERIFICO SIN SON IGUALES
                if matriz[1][j] > matriz[1][j+1]: #TOMO EN CUENTA LA LISTA 2 AHORA
                    #INTERCAMBIAR LISTA2 
                    menor2 = matriz[1][j+1]
                    matriz[1][j+1] = matriz[1][j]
                    matriz[1][j] = menor2
                    #INTERCAMBIAR LISTA1 PARA QUE ESTEN ENLAZADAS 
                    menor = matriz[0][j+1]
                    matriz[0][j+1] = matriz[0][j]
                    matriz[0][j] = menor 

        if intercambio == False: 
            break 

        matriz = [matriz[0],matriz[1]]
    
    return matriz 