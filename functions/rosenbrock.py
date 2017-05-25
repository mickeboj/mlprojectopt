import math
import numpy as np

def obj_fun(x):
    first_sum = 0.0
    second_sum = 0.0
    for c in range(len(x)-1):
        first_sum += 100.0*(x[c+1]-x[c]**2.0)**2.0
        second_sum += (1-x[c])**2.0

    return first_sum + second_sum

def get_grad(x):
    grad = []
    for i in range(len(x)-1):
        if i == 0:
            grad.append(-400.0*x[i]*(x[i+1]-x[i]**2.0)-2.0*(1-x[i]))
        else:
            grad.append(200.0*(x[i]-x[i-1]**2.0)-400.0*x[i]*(x[i+1]-x[i]**2.0)-2.0*(1-x[i]))

    grad.append(200.0*(x[-1]-x[-2]**2.0))
    return np.array(grad)

def get_opt_min():
    return 0.0

def get_bounds():
    return -30,30

def name():
    return "Rosenbrock function"
