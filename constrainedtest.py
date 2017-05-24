from solvers import GA,BFGS,LBFGSB
from functions import constrained
from tests import stabilitytest, accuracytest, dimensiontest
from pyevolve import Initializators, Mutators, Crossovers, Scaling

dimension = 3


def set_genome_par(genome,bounds):
    genome.setParams(rangemin=bounds[0],rangemax=bounds[1])
    genome.initializator.set(Initializators.G1DListInitializatorReal)
    genome.mutator.set(Mutators.G1DListMutatorRealGaussian)
    genome.crossover.set(Crossovers.G1DListCrossoverRealSBX)

def set_ga_par(ga):
    ga.setGenerations(200)
    ga.setMutationRate(0.12)
    ga.setPopulationSize(200)
    ga.getPopulation().scaleMethod.set(Scaling.SigmaTruncScaling)


def get_Gsolv(dim):
    Gsolv = GA.Genetic_Solver()
    Gsolv.set_fun(constrained.obj_fun,dim,0)
    set_genome_par(Gsolv.genome,constrained.get_bounds())
    Gsolv.set_instance()
    set_ga_par(Gsolv.ga)
    return Gsolv

Bsolv = SLSQP.SLSQP()
Bsolv.set_dim(dimension)
Bsolv.set_obj_fun(constrained.obj_fun_unmerged)
Bsolv.set_constraints(constrained.get_fun_constraints())
Bsolv.set_opt(False,300)
Bsolv.set_grad(constrained.get_grad_unmerged)
Bsolv.set_bnds(constrained.get_bounds_tuple)




if __name__ == '__main__':
    # Stabtest = stabilitytest.STest(get_Gsolv,Bsolv,constrained.get_bounds(),
    # dimension,10,constrained.name())
    # Stabtest.run()
    # Stabtest.print_res()
    #
    # Acctest = accuracytest.ATest(get_Gsolv,Bsolv,constrained.get_bounds(),
    #                             dimension,10,constrained.get_opt_min(),constrained.name())
    # Acctest.run()
    # Acctest.print_res()
    # Acctest.plot_res()

    Dimtest = dimensiontest.DTest(get_Gsolv,Bsolv,constrained.get_bounds(),range(2,13),constrained.get_opt_min(),constrained.name())
    Dimtest.run()
    Dimtest.print_res()
    Dimtest.plot_res()
