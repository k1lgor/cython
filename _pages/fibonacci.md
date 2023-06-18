---
layout: page
title: Fibonacci
permalink: /fibonacci/
---

The Fibonacci benchmark focuses on comparing the execution time and performance between Python and Cython implementations for generating Fibonacci numbers. The `fibonacci_benchmark.py` script measures the execution time of Fibonacci number generation for a given input and provides insights into the speed improvements achieved by using Cython.

The purpose of this benchmark is to quantify the performance gains obtained by leveraging the static typing and optimizations offered by Cython in Fibonacci number calculations.

To run the Fibonacci benchmark, follow the instructions below:

1. Ensure that you have Python and Cython installed on your system. Refer to the installation instructions in the repository's [README.md](https://github.com/k1lgor/cython/blob/main/README.md) for more information.
2. Clone the repository to your local machine.
3. Open a terminal and navigate to the location of the `fibonacci_benchmark.py` script.
4. Run the script using the appropriate Python command (e.g., `python fibonacci_benchmark.py`).
5. The script will execute the Fibonacci number generation for a specified input and measure the execution time for both Python and Cython implementations.
6. The output will display the execution times for each implementation and saved in `fibonacci_output.txt`, allowing you to observe the performance differences between Python and Cython.

Feel free to experiment with different input values and compare the execution times to gain insights into the speed improvements achieved by utilizing Cython for Fibonacci number generation.
