import math
import numpy as np
import scipy.io


tempA = scipy.io.loadmat('Amat.mat')
A = tempA['As']
tempB = scipy.io.loadmat('Bmat.mat')
b = tempB['b']
tempC = scipy.io.loadmat('Cmat.mat')
c = tempC['c']
tempH = scipy.io.loadmat('Hi.mat')
hi_bnds = tempH['hi']
tempL = scipy.io.loadmat('Lo.mat')
lo_bnds = tempL['lo']

def get_A():
    return A

def get_b():
    return b

def get_c():
    return c

def get_hi_bnds():
    return hi_bnds

def get_low_bnds():
    return lo_bnds

def get_opt_min():
    return  -4.6475314286E+02

def check_constraints_bnds(x):
    if (np.dot(A,x) == b).all():
        if(x <= hi_bnds).all():
            if(x >= lo_bnds).all():
                return True
    return False

def obj_fun(x):
    z = np.array(x.genomeList)
    z = z.reshape(1,51)
    return np.dot(z,c)[0][0]


def dum_fun(x):
    return 0.0

def get_bounds():
    return (-0.1,0.0)


def name():
    return "affiro LP problem"
