# EJERCICIO 1
def ordenar_nombre_ascedente(lista_nombres:list, lista_edades:list) -> list: 
    #Recibe por parametro dos listas, una de nombres y otra de edades
    #Ordena los elementos por nombre de manera ascedente 
    #Devuelve la listas ordenadas 
    #USO EL BUBBLE SORT 
    if type(lista_nombres) != list or type(lista_edades) != list:
        print("Uno de los paramentros recididos no es el tipo correcto")
        return None 
    n = len(lista_nombres)
    for i in range(n):
        intercambio = False 
        for j in range(n - i - 1):
            if lista_nombres[j] > lista_nombres [j+1]:
                intercambio = True
                menor_edad = lista_edades[j+1]
                nombre_menor = lista_nombres[j+1]

                lista_nombres[j+1] = lista_nombres[j]
                lista_edades[j+1] = lista_edades[j]

                lista_nombres[j] = nombre_menor
                lista_edades[j] = menor_edad
        if intercambio == False:
            break 
    mi_matriz = [lista_nombres, lista_edades]
    return mi_matriz 