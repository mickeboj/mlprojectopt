import math
from pyevolve import Initializators, Mutators, Crossovers

def obj_fun(x):
    x1 = x[0]
    x2 = x[1]
    term1 = 100*math.sqrt(abs(x2-0.01*x1**2))
    term2 = 0.01*abs(x1+10)
    return term1+term2

def get_bounds():
    return -15,3

def set_genome_par(genome,bounds):
    genome.setParams(rangemin=bounds[0],rangemax=bounds[1])
    genome.initializator.set(Initializators.G1DListInitializatorReal)
    genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
    genome.crossover.set(Crossovers.G1DListCrossoverRealSBX)

def set_ga_par(ga):
    ga.setGenerations(200)
    ga.setMutationRate(0.2)
    ga.setPopulationSize(500)
