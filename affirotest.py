from solvers import GA_Const,BFGS
from functions import affiro
from tests import stabilitytest, accuracytest, timetest, dimensiontest
from pyevolve import Initializators, Mutators, Crossovers, Scaling
from random import uniform

dimension = 51


def const_init(genome, **args):
    range_min = genome.getParam("rangemin", 0)
    range_max = genome.getParam("rangemax", 100)
    while True:
        res = [uniform(range_min, range_max) for i in xrange(genome.getListSize())]
        if affiro.check_constraints_bnds(res):
            print "One created"
            break
    genome.genomeList = res

def set_genome_par(genome,bounds):
    genome.setParams(rangemin=bounds[0],rangemax=bounds[1])
    genome.initializator.set(const_init)
    genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
    genome.crossover.set(Crossovers.G1DListCrossoverRealSBX)

def set_ga_par(ga):
    ga.setGenerations(10)
    ga.setMutationRate(0.12)
    ga.setPopulationSize(10)
    ga.getPopulation().scaleMethod.set(Scaling.SigmaTruncScaling)


def get_Gsolv(dim):
    Gsolv = GA_Const.Genetic_Solver()
    Gsolv.set_fun(affiro.obj_fun,dim,1)
    set_genome_par(Gsolv.genome,(0,1e10))
    Gsolv.set_instance(affiro.check_constraints_bnds)
    set_ga_par(Gsolv.ga)
    return Gsolv


if __name__ == '__main__':
    G = get_Gsolv(dimension)
    G.solve()
