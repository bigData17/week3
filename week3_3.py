from __future__ import division; import timeit
import pyximport; pyximport.install()

def sum_withpython1():
    x = 0
    for i in range(10000):
        x = x + 1/((i+1)*(i+1))
    return x

print('Time with sum_withpython1:', timeit.timeit(sum_withpython1, number=500))
print('Time with cython:', timeit.timeit(stmt='sumcython.sum_withcython()', 
                setup='import sumcython', number=500))