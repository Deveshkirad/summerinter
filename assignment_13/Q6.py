# 6) Solve the following equation using linalg() and inverse Matrix method x - 2y + 3z = 9 -x + 3y - z = -6 2x - 5y + 5z = 17 
import numpy as np

A = np.array([
    [1, -2, 3],
    [-1, 3, -1],
    [2, -5, 5]
])

B = np.array([9, -6, 17])

solution = np.linalg.solve(A, B)

print("x =", solution[0])
print("y =", solution[1])
print("z =", solution[2])