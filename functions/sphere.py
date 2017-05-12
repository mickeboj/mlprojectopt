import math
import numpy as np

def obj_fun(x):
    first_sum = 0.0
    for c in x:
        first_sum += c**2
    return first_sum

def get_grad(x):
    grad = []
    for c in x:
        grad.append(2*c)
    return np.array(grad)

def get_opt_min():
    return 0.0

def get_bounds():
    return -6,6

def name():
    return "Sphere function"
