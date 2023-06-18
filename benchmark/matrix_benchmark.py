import timeit

import cython
import numpy as np


def matrix_multiply_python(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)


@cython.cfunc
@cython.locals(matrix1=cython.double[:, :], matrix2=cython.double[:, :])
def matrix_multiply_cython(matrix1, matrix2):
    rows = matrix1.shape[0]
    cols = matrix2.shape[1]
    result = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            for k in range(matrix1.shape[1]):
                result[i, j] += matrix1[i, k] * matrix2[k, j]

    return result


def benchmark():
    matrix_size = [100, 200, 300, 400]

    with open("matrix_output.txt", "w") as f:
        for size in matrix_size:
            f.write(f"size = {size}\n")
            matrix1 = np.random.rand(size, size)
            matrix2 = np.random.rand(size, size)

            python_time = timeit.timeit(lambda: matrix_multiply_python(matrix1, matrix2), number=1)
            cython_time = timeit.timeit(lambda: matrix_multiply_cython(matrix1, matrix2), number=1)

            f.write(f"Matrix Size: {matrix_size}x{matrix_size}\n")
            f.write(f"Python Time: {python_time:.6f} seconds\n")
            f.write(f"Cython Time: {cython_time:.6f} seconds\n")

            speedup = (python_time - cython_time) / python_time * 100
            if speedup >= 0:
                f.write(f"Cython is {speedup:.2f}% faster than Python\n")
            else:
                f.write(f"Python is {-speedup:.2f}% faster than Cython\n")


if __name__ == "__main__":
    benchmark()
