import timeit

import numpy as np

import cython


def computing_columns(matrix):
    num_cols = matrix.shape[1]
    means = np.zeros(num_cols)
    for col in range(num_cols):
        means[col] = np.mean(matrix[:, col])

    return means


@cython.cfunc
@cython.locals(num_cols=cython.int, means=cython.double)
def computing_columns_cython(matrix):
    num_cols = matrix.shape[1]
    means = np.zeros(num_cols)
    for col in range(num_cols):
        means[col] = np.mean(matrix[:, col])

    return means


def benchmark():
    numbers = [1000, 2000, 3000, 4000, 5000]

    with open("computing_columns.txt", "w") as f:
        for n in numbers:
            np.random.seed(0)
            rows, cols = n, n
            matrix = np.random.rand(rows, cols)

            f.write(f"rows, cols = {rows, cols}\n")

            python_time = timeit.timeit(lambda: computing_columns(matrix), number=1)
            cython_time = timeit.timeit(
                lambda: computing_columns_cython(matrix), number=1
            )

            f.write(f"Python: {python_time:.6f} seconds\n")
            f.write(f"Cython: {cython_time:.6f} seconds\n")

            speedup = (python_time - cython_time) / python_time * 100
            if speedup >= 0:
                f.write(f"Cython is {speedup:.2f}% faster than Python\n")
            else:
                f.write(f"Python is {-speedup:.2f}% faster than Cython\n")


if __name__ == "__main__":
    benchmark()
