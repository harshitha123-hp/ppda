import numpy as np

# Create two 3x3 matrices with random integers between 1 and 10
matrix1 = np.random.randint(1, 11, size=(3, 3))
matrix2 = np.random.randint(1, 11, size=(3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix Subtraction
matrix_sub = matrix1 - matrix2
print("\nMatrix Subtraction (Matrix1 - Matrix2):")
print(matrix_sub)

# Element-wise Division
matrix_div = matrix1 / matrix2
print("\nElement-wise Division (Matrix1 / Matrix2):")
print(matrix_div)
