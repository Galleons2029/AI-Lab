# MITx 6.86x
### Machine Learning with Python-From Linear Models to Deep Learning

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

conda create -n 6.86x python=3.8
Note: As mentioned above, you may use other versions of python, as long as functions available only in 3.9+ are not used.

To activate this environment, use

conda activate 6.86x
Finally, install all of the required packages:

```
conda install pytorch -c pytorch
conda install numpy
conda install matplotlib
conda install scipy
conda install tqdm
conda install scikit-learn
```



# MIT6.s191
## Instructions
MIT Introduction to Deep Learning software labs are designed to be completed at your own pace. At the end of each of the labs, there will be instructions on how you can submit your materials as part of the lab competitions. These instructions include what information must be submitted and in what format.

## Opening the labs in Google Colaboratory:

The 2023 Introduction to Deep Learning labs will be run in Google's Colaboratory, a Jupyter notebook environment that runs entirely in the cloud, so you don't need to download anything. To run these labs, you must have a Google account.

On this Github repo, navigate to the lab folder you want to run (`lab1`, `lab2`, `lab3`) and open the appropriate python notebook (\*.ipynb). Click the "Run in Colab" link on the top of the lab. That's it!

## Running the labs
Now, to run the labs, open the Jupyter notebook on Colab. Navigate to the "Runtime" tab --> "Change runtime type". In the pop-up window, under "Runtime type" select "Python 3", and under "Hardware accelerator" select "GPU". Go through the notebooks and fill in the `#TODO` cells to get the code to compile for yourself!
