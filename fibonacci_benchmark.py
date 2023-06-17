import timeit

import cython


def fib_python(n):
    return n if n <= 1 else fib_python(n - 1) + fib_python(n - 2)


@cython.cfunc
@cython.locals(n=cython.int)
def fib_cython(n):
    return n if n <= 1 else fib_cython(n - 1) + fib_cython(n - 2)


def benchmark():
    numbers = [10, 20, 30]

    with open("benchmark_output.txt", "w") as f:
        for n in numbers:
            f.write(f"n = {n}\n")

            python_time = timeit.timeit(lambda: fib_python(n), number=1)
            cython_time = timeit.timeit(lambda: fib_cython(n), number=1)

            f.write(f"Python: {python_time:.6f} seconds\n")
            f.write(f"Cython: {cython_time:.6f} seconds\n")

            speedup = (python_time - cython_time) / python_time * 100
            if speedup >= 0:
                f.write(f"Cython is {speedup:.2f}% faster than Python\n")
            else:
                f.write(f"Python is {-speedup:.2f}% faster than Cython\n")


if __name__ == "__main__":
    benchmark()
