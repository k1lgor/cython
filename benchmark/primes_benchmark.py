import math
import timeit

import cython


# Python implementation
def generate_primes_python(n):
    return [
        num
        for num in range(2, n)
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
    ]


# Cython implementation
@cython.cfunc
@cython.locals(n=cython.int)
def generate_primes_cython(n):
    return [
        num
        for num in range(2, n)
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
    ]


# Benchmark
def benchmark():
    numbers = [10000, 100000, 1000000, 2000000]

    with open("primes_output.txt", "w") as f:
        for n in numbers:
            f.write(f"n = {n}\n")

            # Python benchmark
            python_time = timeit.timeit(lambda: generate_primes_python(n), number=1)

            # Cython benchmark
            cython_time = timeit.timeit(lambda: generate_primes_cython(n), number=1)

            f.write(f"Python time: {python_time:.6f} seconds\n")
            f.write(f"Cython time: {cython_time:.6f} seconds\n")

            speedup = (python_time - cython_time) / python_time * 100
            if speedup >= 0:
                f.write(f"Cython is {speedup:.2f}% faster than Python\n")
            else:
                f.write(f"Python is {-speedup:.2f}% faster than Cython\n")


if __name__ == "__main__":
    # Run the benchmark
    benchmark()
