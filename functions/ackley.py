import math
import numpy as np

def obj_fun(x):
    first_sum = 0.0
    second_sum = 0.0
    for c in x:
        first_sum += c**2.0
        second_sum += math.cos(2.0*math.pi*c)
    n = float(len(x))
    return -20.0*math.exp(-0.2*math.sqrt(first_sum/n)) - math.exp(second_sum/n) + 20.0 + math.e

def get_grad(x):
    grad = []
    first_sum = 0.0
    second_sum = 0.0
    for c in x:
        first_sum += c**2.0
        second_sum += math.cos(2.0*math.pi*c)
    n = float(len(x))
    for c in x:
        grad.append(20.0*0.2/math.sqrt(n)*c/math.sqrt(first_sum)*math.exp(-0.2*math.sqrt(first_sum/n)) +
        2.0*math.pi/n*math.sin(2.0*math.pi*c)*math.exp(second_sum/n))
    return np.array(grad)

def get_opt_min():
    return 0.0

def get_bounds():
    return -32,32

def name():
    return "Ackley's Function"
