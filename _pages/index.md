---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Python vs Cython Benchmark
permalink: /
---

## **Description**

This repository contains a collection of benchmark scripts to compare the performance between Python and Cython implementations. The benchmark focuses on measuring the execution time of various algorithms and tasks implemented in both Python and Cython, highlighting the potential performance improvements achieved by using Cython.

## **Key Features**

- Benchmark scripts for different algorithms and tasks implemented in Python and Cython.
- Performance measurements for each benchmark, including execution time comparisons.
- Detailed documentation and explanations of the benchmarking methodology.
- Instructions for running the benchmarks and interpreting the results.
- Sample code showcasing the usage of Python and Cython for performance optimization.

## **Purpose**

The main purpose of this repository is to provide developers and enthusiasts with a practical reference for understanding the performance differences between Python and Cython. By comparing the execution times of various scripts implemented in both languages, users can gain insights into the potential speed improvements that can be achieved by utilizing Cython's static typing and optimizations.

## **How to Use**

To run the benchmark, follow these steps:

1. Make sure you have Python and Cython installed on your machine.
    - <u>Unix/Linux</u>
        - Python Installation

            ```bash
            # Check if Python and pip are already installed
            python3 --version
            pip3 --version

            # If Python and pip are not installed, install using package manager
            # For Debian/Ubuntu
            sudo apt update
            sudo apt install python3 python3-pip 

            # For RedHat/Fedora/CentOS
            sudo dnf update
            sudo dnf install python3 python3-pip 

            # For Arch/Manjaro
            sudo pacman -Sy python python-pip 

            # For OpenSUSE
            sudo zypper refresh
            sudo zypper install python3 python3-pip 
            
            ```

        - Cython Installation

            ```bash
            # Install Cython using pip
            pip3 install cython
            ```

    - <u>macOS</u>
        - Python Installation

            ```bash
            # Check if Python and pip are already installed
            python3 --version
            pip3 --version

            # If Python and pip are not installed, install using Homebrew
            brew update
            brew install python python-pip
            ```

        - Cython Installation

            ```bash
            pip install cython
            ```

    - <u>Windows</u>
        - Python Installation
            1. Go to the official Python website: <https://www.python.org/downloads/windows/>
            2. Download the latest Python installer for Windows.
            3. Run the installer and follow the installation instructions. Make sure to check the box that adds Python to the system PATH.

        - Cython Installation

            ```powershell
            # Install Cython using pip
            pip install cython
            ```

2. Clone this repository to your local machine.

    ```bash
    git clone git@github.com:k1lgor/cython.git
    ```

3. Navigate to the repository's directory.

    ```bash
    cd cython
    ```

4. Open a terminal and run the following command to execute the benchmark:

   ```bash
   cd benchmark
   python <filename>.py
   ```

## **Automatic Trigger (Workflow)**

A GitHub Actions workflow has been set up to automatically run the benchmarks and generate the performance results. The workflow is triggered whenever changes are pushed to the repository's main branch. The benchmark results, including execution times and performance comparisons, are saved as artifacts and can be accessed from the Actions tab in the repository.

## **Contribution**

Contributions to this repository are welcome! If you have additional benchmark scripts, performance optimizations, or improvements to the existing benchmarks, feel free to submit a pull request. Please ensure that the benchmarks follow the established guidelines and provide clear documentation for reproducibility and accuracy.

## **License**

This repository is licensed under the [MIT License](https://github.com/k1lgor/cython/blob/main/LICENSE), allowing users to freely use, modify, and distribute the benchmark scripts. However, it's recommended to review the license file in the repository for more information.

## **Disclaimer**

The benchmark results may vary depending on the specific hardware, software configuration, and optimization techniques used. The purpose of this repository is to provide general insights and comparisons between Python and Cython, but individual results may differ. Users are encouraged to conduct their own benchmarks and performance measurements based on their specific use cases and requirements.
