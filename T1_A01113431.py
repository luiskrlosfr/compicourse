# coding=utf-8
# Luis Carlos Figueroa Rodríguez, A01113431
# Diseño de Compiladores (A3-101, Gpo. 1)
# 21 / 01 / 2019
# Tarea 1
import queue

# ------------------ Stack ------------------>


# Un stack o pila es una estructura de datos con el formato LIFO
# (Last Input - First Output) en la que el último dato que entra en la
# pila es el primero en salir.

# Python utiliza listas, las cuales se pueden adaptar para crear un stack.
stack = [] # Crea una stack vacío

stack = [1, 2, 3] # Crea un stack con los números 1, 2 y 3, siendo 1 el primer elemento y 3 el último insertado

stack.pop() # Saca al último elemento insertado en el stack (3)

stack.append(4) # Inserta el elemento 4 al stack

s = []
if not s:   # Es una forma de verificar si el stack está vacío pero no existe un metodo tal cual
    print("Stack is empty")

# <------------------ Queue ------------------>


# Una queue o fila es una estructura de datos con el formato FIFO (First Input - First Output) en 
# el que el primer elemento insertado en la lista será el primero en salir.

# Se importa la libreria "queue" en la línea 5 de este archivo para poder
# utilizar Queues
q = queue.Queue() # Crea una queue vacía
q.empty() # Verifica si la queue está vacía. Regresa True en caso de que así sea

q.put(5)  # Inserta un elemento (5) a la queue
q.put(6)
q.put(7)
q.put(8)
q.put(9)
q.put(10)

q.qsize() # Regresa el tamaño de la queue

last = q.get() # Saca de la queue el elemento más antigüo de la queue (5) y lo regresa

q.full() # Verifica si la queue está llena. Regresa True en caso de que así sea

# ------------------ Dictionary ------------------>


# Un dictionary o diccionario es una estructura de almacenamiento que permite guardar datos 
# según una llave para poder acceder a sus valores de una forma alternativa. Son parecidos a
# los arreglos, sólo que el índice en vez de ser un número es una llave, la cual puede ser 
# número o incluso string.

# Python incluye diccionarios, por lo que no es necesario importarlos
dicti = {} # Crea un dictionary vacio

dicti["Luis"] = "Carlos" # Agrega al dictionary el valor Carlos para la llave Luis

dicti["Luis"] = 10 # Sobreescribe el valor guardado en la llave Luis por un 10 (porque la llave existía)
dicti["Carlos"] = "Figueroa"
dicti[100] = "Exam"

dicti[100] # Regresa el valor correspondiente a la llave pasada como parámetro

dicti.keys() # Inserta todas las llaves del dictionary en una lista y regresa esa lista

dicti.values() # Inserta todos los valores del dictionary en una lista y regresa esa lista

remove = dicti.pop(100) # Borra del dictionary la llave (y su valor) pasada como argumento. Regresa el valor que le corresponde a esa llave

dicti.items() # Genera una lista de tuplas (key, value) del dictionary

dicti2 = {"Jesus":250}
dicti.update(dicti2) # Inserta todos los key-value del dictionary pasado como parametro al dictionary que llama al metodo

dicti.clear() # Borra todo el contenido del dictionary

# Referencias
# Python. Data Structures. Retrieved from https://docs.python.org/3.6/tutorial/datastructures.html
# Python. Data Structures. Retrieved from https://docs.python.org/3.6/library/queue.html
# Python. Data Structures. Retrieved from https://docs.python.org/3.6/library/stdtypes.html#typesmapping