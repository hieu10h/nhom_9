import numpy as np
from sympy import symbols, Eq, solve, Matrix

# Giải hệ phương trình tuyến tính Ax = b
def solve_linear_equation(A, b):
    # Sử dụng NumPy để giải nghiệm
    x = np.linalg.solve(A, b)
    return x

# Tính ma trận nghịch đảo
def calculate_inverse_matrix(A):
    # Sử dụng NumPy để tính ma trận nghịch đảo
    A_inverse = np.linalg.inv(A)
    return A_inverse

# Tính giá trị riêng và vector riêng
def calculate_eigen(A):
    # Sử dụng SymPy để tính giá trị riêng và vector riêng
    A_sym = Matrix(A)
    eigenvals = A_sym.eigenvals()
    eigenvects = A_sym.eigenvects()
    return eigenvals, eigenvects

# Tính định thức của ma trận
def calculate_determinant(A):
    # Sử dụng SymPy để tính định thức
    A_sym = Matrix(A)
    determinant = np.linalg.det.det()
    return determinant

# Tính cơ sở và không gian cột của ma trận
def calculate_basis_column_space(A):
    # Sử dụng SymPy để tính cơ sở và không gian cột
    A_sym = Matrix(A)
    nullspace = A_sym.nullspace()
    columnspace = A_sym.columnspace()
    return nullspace, columnspace

# Ví dụ sử dụng các chức năng
A = np.array([[2, 1], [1, -1]])
b = np.array([3, 1])

# Giải hệ phương trình tuyến tính
solution = solve_linear_equation(A, b)
print("Nghiệm của hệ phương trình:")
print(solution)

# Tính ma trận nghịch đảo
A_inverse = calculate_inverse_matrix(A)
print("Ma trận nghịch đảo:")
print(A_inverse)

# Tính giá trị riêng và vector riêng
eigenvals, eigenvects = calculate_eigen(A)
print("Giá trị riêng:")
print(eigenvals)
print("Vector riêng:")
print(eigenvects)

# Tính định thức của ma trận
determinant = calculate_determinant(A)
print("Định thức của ma trận:")
print(determinant)

# Tính cơ sở và không gian cột của ma trận
nullspace, columnspace = calculate_basis_column_space(A)
print("Cơ sở không gian cột:")
print(nullspace)
print("Không gian cột:")
print(columnspace)
