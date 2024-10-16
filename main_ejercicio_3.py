#EJERCICIO 3

#DADAS LAS SIGUIENTES LISTAS 
estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", 
               "Eugenia", "Soledad", "Mario", "María"]
apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui",
                "Mitre","Andrade","Loza","Antares","Roca","Perez"]
nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

# Desarrollar una función que realice el ordenamiento de las listas por apellido de
# manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
# ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
# descendente.

from modulo.ejercicio_3 import * 

matriz_desordenada = [estudiantes, apellidos, nota]
matriz_ordenada_nombres = ordenar_x_3_condiciones(matriz_desordenada)

print("Lista ordenada: ")
for i in range (len(estudiantes)):
    print([estudiantes[i],apellidos[i],nota[i]]) 