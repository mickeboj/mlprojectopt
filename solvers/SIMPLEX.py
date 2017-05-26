from scipy.optimize import minimize
from numpy.random import random as r


class SIMPLEX(object):


    def __init__(self):
        self.obj_fun=None
        self.dim = None
        self.options = None
        self.grad = None
        self.constraints = None
        # self.bnds_fun= None

    def set_obj_fun(self,fun):
        self.obj_fun=fun

    def set_constraints(self,cons):
        self.constraints = cons

    def set_dim(self,dim):
        self.dim=dim

    def set_grad(self,grad):
        self.grad = grad

    # def set_bnds(self,bnds_fun):
    #     self.bnds_fun = bnds_fun

    def set_opt(self,disp,maxiter=None):
        d = {}
        d['disp'] = disp
        #d['gtol'] = 1e-6
        if maxiter:
            d['maxiter']=maxiter
        self.options = d

    def name(self):
        return "nelder-mead"


    def solve(self,bounds):
        x0=[]
        # bnds = self.bnds_fun(self.dim)
        for i in range(self.dim):
            x0.append(bounds[1] - r(1)[0]*(bounds[1]-bounds[0]))
        res = minimize(self.obj_fun,x0,method='nelder-mead',jac=self.grad,constraints=self.constraints,options=self.options,tol=1e-22, bounds=bounds)
        return res.fun
