import math
import numpy as np

def obj_fun(x):
    n = float(len(x))
    first_prod = 0.0
    constraint_sum = 0.0
    for c in x:
        first_prod = first_prod *c
        constraint_sum+= c**2
    return -(math.sqrt(n)**n)*first_prod + constraint_sum -1

def obj_fun_unmerged(x):
    n = float(len(x))
    first_prod = 0.0
    for c in x:
        first_prod = first_prod *c
    return -(math.sqrt(n)**n)*first_prod

def get_fun_constraints():
    cons = ({'type': 'eq',
            'fun' : lambda x: np.array(x**2 - 1),
            'jac' : lambda x: np.array(2.0*x)})
    return cons

def get_grad_unmerged(x):
    grad = []
    n = float(len(x))
    prod = 1.0
    for c in x:
        prod*=c
    for c in x:
        grad.append((math.sqrt(n)**n)*prod/c)
    return np.array(grad)


def get_grad(x):
    grad = []
    n = float(len(x))
    prod = 1.0
    for c in x:
        prod*=c
    for c in x:
        grad.append((math.sqrt(n)**n)*prod/c+2*c)
    return np.array(grad)

def get_opt_min():
    return 1.0

def get_bounds():
    return 0,1

def name():
    return "G3 constraint function"
