from solvers import GA_Const,BFGS
from functions import affiro
from tests import stabilitytest, accuracytest, timetest, dimensiontest
from pyevolve import Initializators, Mutators, Crossovers

dimension = 51

def set_genome_par(genome,bounds):
    genome.setParams(rangemin=bounds[0],rangemax=bounds[1])
    genome.initializator.set(Initializators.G1DListInitializatorReal)
    genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
    genome.crossover.set(Crossovers.G1DListCrossoverRealSBX)

def set_ga_par(ga):
    ga.setGenerations(10)
    ga.setMutationRate(0.12)
    ga.setPopulationSize(10)


def get_Gsolv(dim):
    Gsolv = GA_Const.Genetic_Solver()
    Gsolv.set_fun(affiro.obj_fun,dim,1)
    set_genome_par(Gsolv.genome,(0,1e20))
    Gsolv.set_instance(affiro.check_constraints_bnds)
    set_ga_par(Gsolv.ga)
    return Gsolv


if __name__ == '__main__':
    G = get_Gsolv(dimension)
    G.solve()
