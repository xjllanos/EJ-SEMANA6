#EJERCICIO 3 
def ordenar_x_3_condiciones(matriz_desordenada:list)->list: 
    lista_estudiantes = matriz_desordenada[0]
    lista_apellidos = matriz_desordenada[1]
    lista_nota = matriz_desordenada[2]

    for i in range(len(lista_estudiantes)):
        for j in range(0,len(lista_estudiantes) - i - 1):
            if lista_apellidos[j] > lista_apellidos[j+1]: #ORDENO POR ASCEDENTE LOS APELLIDOS
                ordenar_ascedente(lista_apellidos,j)
                ordenar_ascedente(lista_estudiantes,j)
                ordenar_ascedente(lista_nota,j)

            elif lista_apellidos[j] == lista_apellidos[j+1]: #VERIFICO SI LOS APELLIDOS SON IGUALES 
                if lista_estudiantes[j] > lista_estudiantes[j+1]: #ORDENO ASCENDENTE POR NOMBRE
                    ordenar_ascedente(lista_estudiantes,j)
                    ordenar_ascedente(lista_apellidos,j)
                    ordenar_ascedente(lista_nota,j)

                
                elif lista_estudiantes[j] == lista_estudiantes[j+1]: #VERIFIFOCO SI NOMBRE Y APELLIDO SON IGUALES
                    if lista_nota[j] < lista_nota[j+1]: #ORDENO POR NOTA DESCENDENTE
                        ordenar_descendente(lista_estudiantes,j)
                        ordenar_descendente(lista_apellidos,j)
                        ordenar_descendente(lista_nota,j)
    return matriz_desordenada

def ordenar_ascedente(lista,j):
    menor = lista[j+1]
    lista[j+1] = lista[j]
    lista[j] = menor 

def ordenar_descendente(lista,j): 
    mayor = lista[j]
    lista[j] = lista[j+1]
    lista[j+1] = mayor 
            