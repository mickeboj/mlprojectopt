import math
import numpy as np

def obj_fun(x):
    first_sum=0.0
    for i in range(len(x)):
        first_sum +=(x[i]**2-(i+1))**2
    return first_sum

def get_grad(x):
    grad=[]
    for i in range(len(x)):
        grad.append(4*x[i]*(x[i]**2-(i+1)))
    return np.array(grad)

def get_opt_min():
    return 0.0

def get_bounds():
    return -500,500

def name():
    return "Qing function"
