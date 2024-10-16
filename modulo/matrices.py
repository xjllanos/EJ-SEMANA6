#CARGO METODOS PARA MANIPULAR MATRICES 
def mostrar_matriz(matriz: list) -> None:
    if type(matriz) != list: # es importante verificar que el elemento sea del tipo lista    
        print("La función debe recibir una lista")
        return None
    # accede a las filas
    for i in range(len(matriz)):
        # accede a los elementos de cada columna en una fila
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print(" ")

def inicializar_matriz(cant_filas: int, cant_columnas:int, valor_inicial: any = 0) -> list:
    matriz = []
    for i in range(cant_filas):
        fila = [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz
    
def cargar_matriz_secuencialmente(matriz: list) -> list:  
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"Ingrese un número para la fila={i}, columna= {j}: ")) 
    return matriz

def cargar_aleatoriamente(matriz: list) -> list:    
    if type(matriz) != list: # es importante verificar que el elemento sea del tipo lista    
        print("La función debe recibir una lista")
        return None
    seguir = "s"
    while seguir == "s":
        fila = int(input("Ingrese fila: "))
        columna = int(input("Ingrese columna: "))
        numero = int(input("Ingrese número: "))
        matriz[fila][columna] = numero
        seguir = input("Desea seguir cargando numeros: s/n ")
    return matriz

def buscar_lineal_matriz(matriz: list, valor: int) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"{valor} se encuentra en la fila {i},columna {j}")