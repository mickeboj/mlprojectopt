import math
import numpy as np

def obj_fun(x):
    first_sum = 0.0
    second_sum = 0.0
    for c in range(len(x)-1):
        first_sum += 100*(x[c+1]-x[c]**2)**2
        second_sum += (1-x[c])**2

    return first_sum + second_sum

#def get_grad(x):
#    grad = []
#    for c in x:
#        grad.append(2*c)
#    return None

def get_opt_min():
    return 0.0

def get_bounds():
    return -5,10

def name():
    return "Rosenbrock function"
