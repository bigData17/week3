# load relevant libraries
from scipy import optimize
import numpy as np
import pylab

# load data
x,y = np.loadtxt("Points_3.txt", delimiter=" ", unpack=True)

# find parameters for polynomial of degree 3 for the data
parameters = np.polyfit(x, y, 3)

# define the polynomial defined by the parameters
def poly(x):
	return(parameters[0]+parameters[1]*x+parameters[2]*x*x+parameters[3]*x*x*x)

# use Scipy's optimization tool to find the root of the polynomial
sol = optimize.root(poly, 1.0)

# use pylab package to plot the data, the polynomial and the found root. 
pylab.scatter(x, y)
pylab.plot(x, poly(x), '-')
pylab.plot([sol.x], 0, marker='o', markersize=10, color="red")
pylab.show()
