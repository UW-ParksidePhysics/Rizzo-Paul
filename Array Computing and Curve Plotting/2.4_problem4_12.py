# Problem 4
from numpy import zeros, linalg, linspace, sqrt, sin, pi
import matplotlib.pyplot as mp
A = zeros([10, 10])

n = 0
while n <= 10 - 1:
    A[n, n] = 2
    n = n + 1

n = 0
while n <= 10 - 2:
    A[n, n + 1] = 1
    A[n + 1, n] = 1
    n = n + 1

lO = int(input('What npoints? '))
H = (1 / (2 * (1 / (lO - 1)) ** 2)) * A

(V, D) = linalg.eig(H)
B = D[:, [9]]
x = linspace(1/(lO+1), lO/(lO+1), lO)


def y(x):
    y = sqrt(2) * sin(pi * x)
    return y


mp.plot(x, B)  # Blue Graph
mp.plot(x, y(x))  # Orange Graph
mp.show()
