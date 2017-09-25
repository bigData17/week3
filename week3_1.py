# Define a sript reads a matrix from a file and solves the linear matrix equation Ax=b
# Where b is the last column of the input-matrix and A is the other columns.
# import the numpy package and solve function
import numpy as np
from numpy.linalg import solve
# Save the file name to a variable
file = "mat.txt"
A = []
b = []
# Load data from a text file
data = np.genfromtxt(file,delimiter=",")
# Slice the array we got above into two arrays
# Where b is the last column of the input-matrix and A is the other columns.
A= data[:,:len(data)]
b= data[:,len(data)]
# using solve function to solve a linear matrix equation
print (solve(A, b))