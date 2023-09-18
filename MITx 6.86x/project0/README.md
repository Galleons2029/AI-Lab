# Project 0

## Introduction
The goal of this project 0 is to help you set up your python environment and to give you an introduction to the mechanics of the online grading system.

As a reminder, this course assumes a basic understanding of Python at the level of 6.00.1x Introduction to Computer Science and Programming using Python (also on MIT Open CourseWare). This means you should be proficient in the following: functions, tuples and lists, mutability, recursion, dictionaries, and object-oriented programming.

Additionally, we expect you to be able to install the required packages using pip and be comfortable reading the documentation of these packages to find out more about the functions you are not familiar with.
![Alt text](image.png)

## Instruction
Required python packages

Throughout this course, we will be using Python 3.8 along with the following packages. Code written in new versions of python will be accepted, as long as functions/features that are available only in Python 3.9 or beyond are not used.

- NumPy
- matplotlib
- scikit-learn
- SciPy
- tqdm
- PyTorch

Installation using pip

If you already have a working installation of Python 3, you should be able to install all of the above packages using pip.

```
pip3 install numpy
pip3 install matplotlib
pip3 install scipy
pip3 install tqdm
pip3 install scikit-learn
```


For PyTorch, follow the instructions on https://pytorch.org/to install from pip repository corresponding to your system. You will not need CUDA for this course.

In the above commands, you can replace pip3 with python3 -m pip to make sure you are installing the packages for the version of python your system is currently using.

Installation using conda

However, the recommended way of configuring your system is by using a conda environment.

We recommend that you install the latest version of Miniconda from https://docs.conda.io/en/latest/miniconda.html.

You can then create a conda environment for this course using
```
conda create -n 6.86x python=3.8
```
Note: As mentioned above, you may use other versions of python, as long as functions available only in 3.9+ are not used.

To activate this environment, use
```
conda activate 6.86x
```
Finally, install all of the required packages:

```
conda install pytorch -c pytorch
conda install numpy
conda install matplotlib
conda install scipy
conda install tqdm
conda install scikit-learn
```

### Testing your installation

Download project0.tar.gz and untar it in to a working directory. To deal with tar.gz files on windows, you can use 7-zip.

The project0 folder contains two pyhon files.

main.py contains the various functions you will to complete in the next sections of the project

test.py is a script which runs tests

debug.py contains the code for the final problem of this project

Tip: Throughout the whole online grading system, you can assume the NumPy python library is already imported as np.

This project will unfold both on MITx and on your local machine. You are welcome to implement functions locally and then copy+paste your code into the MITx code boxes to fully check correctness and receive your grade for individual function implementations. Alternatively, you can also implement the functions online first and after finishing, copy+paste the solution to your local main.py file. Be wary of the number of attempts you have for each problem, especially if you choose the second development flow.

**How to Test Locally**: 
In your terminal, navigate to the directory where your project files reside. Execute the command **python test.py** to run all the available tests.

For this project, the test.py file will test that all required packages are correctly installed.

Tip: We recommend using a proper IDE for this course such as Visual Studio Code, Pycharm, etc.