def sum_withcython():
    cdef double x
    x = 0.00
    for i in range(10000):
        x = x + 1/((i+1)*(i+1))
    return x 
