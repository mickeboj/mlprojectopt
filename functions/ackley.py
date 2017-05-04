import math
from pyevolve import Initializators, Mutators, Crossovers

def obj_fun(x):
        first_sum = 0.0
        second_sum = 0.0
        for c in x:
            first_sum += c**2.0
            second_sum += math.cos(2.0*math.pi*c)
        n = float(len(x))
        return -20.0*math.exp(-0.2*math.sqrt(first_sum/n)) - math.exp(second_sum/n) + 20.0 + math.e



def get_opt_min():
    return 0.0

def get_bounds():
    return -32,32


def set_genome_par(genome,bounds):
    genome.setParams(rangemin=bounds[0],rangemax=bounds[1])
    genome.initializator.set(Initializators.G1DListInitializatorReal)
    genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
    genome.crossover.set(Crossovers.G1DListCrossoverRealSBX)

def set_ga_par(ga):
    ga.setGenerations(200)
    ga.setMutationRate(0.12)
    ga.setPopulationSize(500)
