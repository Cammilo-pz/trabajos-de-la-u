import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns

def bubble(L):
    o_bubble = 0  
    m = len(L)
    for i in range(m - 1):
        for j in range(m - i - 1):
            o_bubble += 1
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]          
    #print(o_bubble)
    return o_bubble
    
def insertion(L):
    o_insertion = 0
    i = 1
    while i < (len(L)):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            o_insertion += 1
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1
        i += 1
    #print(o_insertion)
    return o_insertion
    
def selection(L):
    o_selection = 0
    for i in range(len(L) - 1):
        min = i
        for j in range(i + 1, len(L)):
            o_selection += 1
            if (L[min] > L[j]):
                min = j
        if min != i:
            L[min], L[i] = L[i], L[min]
            o_selection += 1
    #print(o_selection)
    return o_selection 
    

num_elements = np.arange(100, 1001, 100)
size = num_elements.size
#print(num_elements)
t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)

op_bubble = np.zeros(size)
op_selection = np.zeros(size)
op_insertion = np.zeros(size)

for i, n in enumerate(num_elements):
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    bubble(vector_ord)
    op_bubble[i] = bubble(vector_ord)
    t_final = perf_counter_ns()
    t_bubble[i] = t_final - t_inicio
    
    
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    op_insertion[i] = insertion(vector_ord)
    insertion(vector_ord)
    t_final = perf_counter_ns()
    t_insertion[i] = t_final - t_inicio
    
    
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    selection(vector_ord)
    op_selection[i] = selection(vector_ord)
    t_final = perf_counter_ns()
    t_selection[i] = t_final - t_inicio
    

print("seleccione la gráfica que desea realizar:")
print(" 1 :grafica de la velocidad y la cantidad de datos")
print(" 2 :grafica de la cantidad de operaciones y la cantidad de datos")
selección = int(input())
if selección == 1:
    plt.plot(num_elements, t_bubble, "r-")
    plt.plot(num_elements, t_insertion, "g-")
    plt.plot(num_elements, t_selection, "b-")
    plt.show()
elif selección == 2:
    plt.plot(num_elements, op_bubble, "r-")
    plt.plot(num_elements, op_insertion,"g-")
    plt.plot(num_elements, op_selection, "b-")
    plt.show()
else :
    print(" ERROR! la opción selecionada no es correcta, debe escoger el número 1 o 2")