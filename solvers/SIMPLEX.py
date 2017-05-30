from numpy.random import random as r
from scipy.optimize import linprog
import numpy as np

class SIMPLEX(object):


    def __init__(self):
        self.obj_fun=None
        self.dim = None
        self.options = None
        self.grad = None
        self.constraints = None
        self.A = None
        self.B = None
        self.C = None
        self.Hi = None
        self.Lo = None

    def set_matrices(self,A_mat,B_mat,C_mat,Hi_mat,Lo_mat):
        self.A = A_mat
        self.B = B_mat
        self.C = C_mat
        self.Hi = Hi_mat
        self.Lo = Lo_mat

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
        return "Simplex"


    def solve(self,bounds):
        c = []
        for e in self.C:
            c.append(e[0])
        res = linprog(c,A_eq= self.A.reshape(27,51),b_eq = self.B.reshape(27,1),bounds = (0,1e20))
        return res.fun
