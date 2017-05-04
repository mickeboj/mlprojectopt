from solvers import GA
from functions import ackley
from pyevolve import Initializators, Mutators, Crossovers


if __name__ == '__main__':
    Gsolv = GA.Genetic_Solver()
    Gsolv.set_fun(ackley.obj_fun,20)
    Gsolv.genome.setParams(rangemin=ackley.get_bounds()[0],rangemax=ackley.get_bounds()[1])
    Gsolv.genome.initializator.set(Initializators.G1DListInitializatorReal)
    Gsolv.genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
    Gsolv.genome.crossover.set(Crossovers.G1DListCrossoverTwoPoint)
    Gsolv.set_instance()
    Gsolv.ga.setGenerations(600)
    Gsolv.ga.setMutationRate(0.05)
    Gsolv.ga.setPopulationSize(100)
    Gsolv.ga.evolve(freq_stats=10)
    print Gsolv.ga.bestIndividual()
    print "Best individual found was" ,Gsolv.ga.bestIndividual().getRawScore()
