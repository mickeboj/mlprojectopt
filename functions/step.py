import math
from pyevolve import Initializators, Mutators, Crossovers

def obj_fun(x):
    sum = 0.0
    for c in x:
        sum+= math.floor(abs(c))
    return sum

def get_bounds():
    return -100,100


def get_opt_min():
    return 0.0

def get_bounds():
    return -100,100

def name():
    return "Step Function"
