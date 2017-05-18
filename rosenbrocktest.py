from solvers import GA,BFGS
from functions import rosenbrock
from tests import stabilitytest, accuracytest
from pyevolve import Initializators, Mutators, Crossovers

dimension = 20


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
    Gsolv.set_fun(rosenbrock.obj_fun,dim,0)
    set_genome_par(Gsolv.genome,rosenbrock.get_bounds())
    Gsolv.set_instance()
    set_ga_par(Gsolv.ga)
    return Gsolv

Bsolv = BFGS.BFGS()
Bsolv.set_dim(dimension)
Bsolv.set_obj_fun(rosenbrock.obj_fun)
Bsolv.set_opt(False,300)
#Bsolv.set_grad(rosenbrock.get_grad)




if __name__ == '__main__':
    #Stabtest = stabilitytest.STest(get_Gsolv,Bsolv,sphere.get_bounds(),
    #dimension,100,sphere.name())
    #Stabtest.run()
    #Stabtest.print_res()

    Acctest = accuracytest.ATest(get_Gsolv,Bsolv,rosenbrock.get_bounds(),
                                dimension,10,rosenbrock.get_opt_min(),rosenbrock.name())
    Acctest.run()
    Acctest.print_res()
    Acctest.plot_res()
