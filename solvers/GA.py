from pyevolve import G1DList, GSimpleGA, Selectors
from pyevolve import Initializators, Mutators, Consts
import math

class Genetic_Solver(object):


    def __init__(self):
        self.genome = None
        self.ga = None

    def set_fun(self,fun,dim):
        self.genome = G1DList.G1DList(dim)
        self.genome.evaluator.set(fun)

    def set_instance(self):
        self.ga = GSimpleGA.GSimpleGA(self.genome)
        self.ga.minimax = Consts.minimaxType["minimize"]
    
