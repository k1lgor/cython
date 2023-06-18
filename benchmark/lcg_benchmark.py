import timeit

import cython


def lcg_python(n):
    a = 1664525
    c = 1013904223
    m = 2**32

    numbers = []
    x = timeit.default_timer()

    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x)

    return numbers


@cython.cfunc
@cython.locals(a=cython.int, c=cython.int, m=cython.int, x=cython.double)
def lcg_cython(n):
    a = 1664525
    c = 1013904223
    m = 2**32

    numbers = []
    x = timeit.default_timer()

    for _ in range(n):
        x = (a * x + c) % m
        numbers.append(x)

    return numbers


def benchmark():
    numbers = [1000000, 2000000, 3000000, 4000000]

    with open("lcg_output.txt", "w") as f:
        for n in numbers:
            f.write(f"n = {n}\n")

            python_time = timeit.timeit(lambda: lcg_python(n), number=1)
            cython_time = timeit.timeit(lambda: lcg_cython(n), number=1)

            f.write(f"Python: {python_time:.6f} seconds\n")
            f.write(f"Cython: {cython_time:.6f} seconds\n")

            speedup = (python_time - cython_time) / python_time * 100
            if speedup >= 0:
                f.write(f"Cython is {speedup:.2f}% faster than Python\n")
            else:
                f.write(f"Python is {-speedup:.2f}% faster than Cython\n")


if __name__ == "__main__":
    benchmark()
