from solvers import GA,BFGS
from functions import ackley
from tests import stabilitytest
from pyevolve import Initializators, Mutators, Crossovers

dim = 20



def set_genome_par(genome,bounds):
    genome.setParams(rangemin=bounds[0],rangemax=bounds[1])
    genome.initializator.set(Initializators.G1DListInitializatorReal)
    genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
    genome.crossover.set(Crossovers.G1DListCrossoverRealSBX)

def set_ga_par(ga):
    ga.setGenerations(200)
    ga.setMutationRate(0.12)
    ga.setPopulationSize(200)


def get_Gsolv():
    Gsolv = GA.Genetic_Solver()
    Gsolv.set_fun(ackley.obj_fun,dim,0)
    set_genome_par(Gsolv.genome,ackley.get_bounds())
    Gsolv.set_instance()
    set_ga_par(Gsolv.ga)
    return Gsolv

Gsolv = get_Gsolv()
Bsolv = BFGS.BFGS()
Bsolv.set_dim(dim)
Bsolv.set_obj_fun(ackley.obj_fun)
Bsolv.set_opt(False,300)
Bsolv.set_grad(ackley.get_grad)




if __name__ == '__main__':
    Stabtest = stabilitytest.STest(get_Gsolv,Bsolv,ackley.get_bound(),100)
    Stabtest.run()
    Stabtest.print_res()
