# Problem 3
from numpy import zeros, linalg, linspace, sqrt, sin, pi
import matplotlib.pyplot as mp
A = zeros([5, 5])

n = 0
while n <= 5 - 1:
    A[n, n] = 2
    n = n + 1

n = 0
while n <= 3:
    A[n, n + 1] = 1
    A[n + 1, n] = 1
    n = n + 1

H = (1 / (2 * (1 / (5 - 1)) ** 2)) * A

(V, D) = linalg.eig(H)
B = D[:, [4]]
x = linspace(1/(5+1), 5/(5+1), 5)


def y(x):
    y = sqrt(2) * sin(pi * x)
    return y


mp.plot(x, B)  # Blue Graph
mp.plot(x, y(x))  # Orange Graph
mp.show()

print(H)
print(V)

