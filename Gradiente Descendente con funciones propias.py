# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:28:35 2021

@author: Kathleen Lucía Torres Mancilla
         Francisco Javier Vite Mimila

Linear Solve: Gradiente descendente con funciones propias

Usar funciones propias para el cálculo del producto de matrices y 
la transpuesta de matrices.

"""
A = [[2.0, 1.0, -3.0], [5.0, -4.0, 1.0], [1.0, -1.0, -4.0]]
print(A)
def transpuesta (M):
    height = len(M)
    width = len(M[0])
#Se itera fila por fila y las devuelve en forma de columnas:
    M_t = [[M[row][col] for row in range(0,height)] for col in range(0,width)]
    return M_t
print(transpuesta(A))

'''
def gradient(x, A, b):
	element_1 = np.dot(np.transpose(A),np.dot(A, x))
	element_2 = np.dot(np.transpose(A), b)
	return element_1 - element_2

def linear_solve(M, v, x_start, umbral, max_iter):
    k = 0.002
    for i in range(max_iter):
        print(x_start)
        x_start = x_start - k * gradient(x_start, M, v)
        current_v = np.dot(M,x_start)
        error_np = np.sum(np.abs(current_v-v))
        if error_np < umbral:
            return x_start
    #return x_start

print(linear_solve(A_coef, b_coef, x_sol, 0.001, 10000))
'''