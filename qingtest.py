from solvers import GA,BFGS
from functions import Qing
from tests import stabilitytest, accuracytest, timetest, dimensiontest
from pyevolve import Initializators, Mutators, Crossovers

dimension = 25


def set_genome_par(genome,bounds):
    genome.setParams(rangemin=bounds[0],rangemax=bounds[1])
    genome.initializator.set(Initializators.G1DListInitializatorReal)
    genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
    genome.crossover.set(Crossovers.G1DListCrossoverRealSBX)

def set_ga_par(ga):
    ga.setGenerations(200)
    ga.setMutationRate(0.12)
    ga.setPopulationSize(200)


def get_Gsolv(dim):
    Gsolv = GA.Genetic_Solver()
    Gsolv.set_fun(Qing.obj_fun,dim,0)
    set_genome_par(Gsolv.genome,Qing.get_bounds())
    Gsolv.set_instance()
    set_ga_par(Gsolv.ga)
    return Gsolv

Bsolv = BFGS.BFGS()
Bsolv.set_dim(dimension)
Bsolv.set_obj_fun(Qing.obj_fun)
Bsolv.set_opt(False,300)
Bsolv.set_grad(Qing.get_grad)




if __name__ == '__main__':
    Stabtest = stabilitytest.STest(get_Gsolv,Bsolv,Qing.get_bounds(),
    dimension,100,Qing.name())
    Stabtest.run()
    Stabtest.print_res()
    Stabtest.plot_res()

    Acctest = accuracytest.ATest(get_Gsolv,Bsolv,Qing.get_bounds(),
                                dimension,50,Qing.get_opt_min(),Qing.name())
    Acctest.run()
    Acctest.print_res()
    Acctest.plot_res()

    Timetest = timetest.TTest(get_Gsolv,Bsolv,Qing.get_bounds(),
                                dimension,100,Qing.name())
    Timetest.run()
    Timetest.print_res()
    Timetest.plot_res()

    Dimtest = dimensiontest.DTest(get_Gsolv,Bsolv,Qing.get_bounds(),range(10,201,10),Qing.get_opt_min(),Qing.name())
    Dimtest.run()
    Dimtest.print_res()
    Dimtest.plot_res()
