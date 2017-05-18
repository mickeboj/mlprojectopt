import math
from pyevolve import Initializators, Mutators, Crossovers

def obj_fun(x):
    x1 = x[0]
    x2 = x[1]
    term1 = 100*math.sqrt(abs(x2-0.01*x1**2))
    term2 = 0.01*abs(x1+10)
    return term1+term2

def get_bounds():
    return -15,3

def get_opt_min():
    return 0.0

def name():
    return "Bukin n.6 function"
