import numpy as np

matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])

escalar = np.array(5)

multiplicacion = escalar.dot(matriz)

print(multiplicacion)

def suma (a,b):
    return (a + b)

print(suma(1,2))

def resta (a,b):
    return (a - b)

print(resta(9,8))

print(suma(40,80)+resta(50,30))