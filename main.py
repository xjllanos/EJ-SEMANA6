from modulo import funciones
from modulo import matrices 

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades =  [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

#Ejercicio 1 
#Desarrollar una función que realice el ordenamiento de las listas 
# por nombre de manera ascendente.
mi_matriz_ordenada = funciones.ordenar_nombre_ascedente(nombres, edades)
matrices.mostrar_matriz(mi_matriz_ordenada) 

