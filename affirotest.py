from solvers import GA,SIMPLEX
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
    genome.initializator.set(Initializators.G1DListInitializatorReal)
    genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
    genome.crossover.set(Crossovers.G1DListCrossoverRealSBX)

def set_ga_par(ga):
    ga.setGenerations(10)
    ga.setMutationRate(0.12)
    ga.setPopulationSize(10)
    ga.getPopulation().scaleMethod.set(Scaling.SigmaTruncScaling)


def get_Gsolv(dim):
    Gsolv = GA.Genetic_Solver()
    Gsolv.set_fun(affiro.dum_fun,dim,0)
    set_genome_par(Gsolv.genome,affiro.get_bounds())
    Gsolv.set_instance()
    set_ga_par(Gsolv.ga)
    return Gsolv


Bsolv = SIMPLEX.SIMPLEX()
Bsolv.set_matrices(affiro.get_A(),affiro.get_b(),affiro.get_c(),affiro.get_hi_bnds(),
                    affiro.get_low_bnds())


if __name__ == '__main__':
    Stabtest = stabilitytest.STest(get_Gsolv,Bsolv,affiro.get_bounds(),
    dimension,100,affiro.name())
    Stabtest.run()
    Stabtest.print_res()
    Stabtest.plot_res()

    Acctest = accuracytest.ATest(get_Gsolv,Bsolv,affiro.get_bounds(),
                                dimension,50,affiro.get_opt_min(),affiro.name())
    Acctest.run()
    Acctest.print_res()
    Acctest.plot_res()

    Timetest = timetest.TTest(get_Gsolv,Bsolv,affiro.get_bounds(),
                                dimension,100,affiro.name())
    Timetest.run()
    Timetest.print_res()
    Timetest.plot_res()
    #
    # Dimtest = dimensiontest.DTest(get_Gsolv,Bsolv,ackley.get_bounds(),range(10,201,10),ackley.get_opt_min(),ackley.name())
    # Dimtest.run()
    # Dimtest.print_res()
    # Dimtest.plot_res()
