from scipy.optimize import minimize
from numpy.random import random as r


class BFGS(object):


    def __init__(self):
        self.obj_fun=None
        self.dim = None
        self.options = None

    def set_obj_fun(self,fun):
        self.obj_fun=fun

    def set_dim(self,dim):
        self.dim=dim

    def set_opt(self,disp,maxiter=None):
        d = {}
        d['disp'] = disp
        if maxiter:
            d['maxiter']=maxiter
        self.options = d

    def solve(self,bounds):
        x0=[]
        for i in range(self.dim):
            x0.append(bounds[1] - r(1)[0]*(bounds[1]-bounds[0]))
        res = minimize(self.obj_fun,x0,method='BFGS',options=self.options)
        if self.options['disp']:
            print res.message
        return res.fun
