import math
import numpy as np

def f(w, x):
    return w * x

def g(z):
    return 1 / (1 + math.exp(-z))

def l(y, y_hat):
    return (y - y_hat)**2

def J(w1, w2, x, y):
    return l(y, g(f(w2, g(f(w1, x)))))

w1 = 0.1
w2 = 0.2
x = 35
y = 1

A = [[2, 4], [3, 5], [1,6]]
B = [[1, 2, 3], [4, 3, 2], [6, 5, 4]]
C = [[8, 7, 6], [7, 8, 9]]

A = np.array(A)
B = np.array(B)
C = np.array(C)

print(C @ B @ A)
 