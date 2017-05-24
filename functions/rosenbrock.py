import math
import numpy as np

def obj_fun(x):
    first_sum = 0.0
    second_sum = 0.0
    for c in range(len(x)-1):
        first_sum += 100*(x[c+1]-x[c]**2)**2
        second_sum += (1-x[c])**2

    return first_sum + second_sum

def get_grad(x):
    grad = []
    for i in range(len(x)):
        grad.append(-400*x[i]*(x[i+1]-x[i]**2)+2*(x[i]-1))
    return np.array(grad)

def get_opt_min():
    return 0.0

def get_bounds():
    return -5,10

def name():
    return "Rosenbrock function"
