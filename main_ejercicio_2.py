#Ejercicio 2 

#DADA LAS SIGUIENTES LISTAS 
materias = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales",
            "Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", 
            "Base de Datos", "Ergonomia","Naturaleza"]
puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

# Desarrollar una función que realice el ordenamiento de las listas por nombre de
# manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
# descendente.

from modulo.ejercicio_2 import * 

matriz_desordena = [materias , puntos]

matriz_ordenada_materias = ordenar_x_iguales(matriz_desordena)

print("Lista ordenada:")
for i in range(len(materias)):
    print([materias[i],puntos[i]]) 