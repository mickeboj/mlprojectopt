import math
import numpy as np

def obj_fun(x):
    x1 = x[0]
    x2 = x[1]
    term1 = 100*math.sqrt(abs(x2-0.01*x1**2))
    term2 = 0.01*abs(x1+10)
    return term1+term2

def get_bounds():
    return -15,3

def get_grad(x):
    grad = []
    first_sign = np.sign(x[1]-0.02*x[0]**2)
    first_sqr = math.sqrt(abs(x[1]-0.01*x[0]**2))
    div_x1 = (-x[0]*first_siqn)/first_sqr+0.01*np.sign(x[0]+10)
    div_x2 = 50*first_siqn/first_sqr
    grad.append(div_x1)
    grad.append(div_x2)
    return np.array(grad)

def get_opt_min():
    return 0.0

def name():
    return "Bukin n.6 function"
