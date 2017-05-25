import math
import numpy as np

def obj_fun(x):
    fun = 0.0
    fun = (x[0]-10)**3.0 + (x[1]-20)**3.0
    g = (x[0]-5)**2.0 + (x[1]-5)**2.0 + 100 + (x[0]-5)**2 + (x[1]-5)**2.0 - 82.81
    return fun - g

def obj_fun_unmerged(x):
    fun = 0.0
    fun = (x[0]-10)**3.0 + (x[1]-20)**3.0
    return fun

def get_fun_constraints():
    cons = ({'type': 'ineq', 'fun': lambda x: np.array([-((x[0]-5)**2.0 + (x[1]-5)**2.0 + 100)]),
                             'jac': lambda x: np.array([-2.0*(x[0]-5), -2*(x[1]-5)])},
            {'type': 'ineq', 'fun': lambda x: np.array([-((x[0]-5)**2.0 + (x[1]-5)**2.0 - 82.81)]),
                             'jac': lambda x: np.array([-2.0*(x[0]-5), -2*(x[1]-5)])}
            )
            #'jac' : lambda x: np.array([c*2.0 for c in x])})
    return cons

def get_grad_unmerged(x):
    grad = []
    grad.append(3.0*(x[0]-10)**2.0)
    grad.append(3.0*(x[1]-20)**2.0)
    return np.array(grad)


def get_grad(x):
    grad = []
    div_x1 = 3.0*(x[0]-10)**2.0 - 4.0*(x[0]-5)
    div_x2 = 3.0*(x[1]-20)**2.0 - 4.0*(x[1]-5)
    return np.array(grad)

def get_opt_min():
    return -6961.81388

def get_bounds():
    return 1,100

def get_bounds_tuple(length):
    bnd = tuple(([13,100],[0,100]))
    return bnd

def name():
    return "G6 constraint function"
