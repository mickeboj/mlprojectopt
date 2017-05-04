import math
from pyevolve import Initializators, Mutators, Crossovers

def obj_fun(x):
    sum = 0.0
    for c in x:
        sum+= math.floor(abs(c))
    return sum

def get_bounds():
    return -100,100


def set_genome_par(genome,bounds):
    genome.setParams(rangemin=bounds[0],rangemax=bounds[1])
    genome.initializator.set(Initializators.G1DListInitializatorReal)
    genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
    genome.crossover.set(Crossovers.G1DListCrossoverRealSBX)

def set_ga_par(ga):
    ga.setGenerations(200)
    ga.setMutationRate(0.12)
    ga.setPopulationSize(500)
