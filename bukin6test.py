from solvers import GA
from functions import bukin6


Gsolv = GA.Genetic_Solver()
Gsolv.set_fun(bukin6.obj_fun,2)
bukin6.set_genome_par(Gsolv.genome,bukin6.get_bounds())
Gsolv.set_instance()
bukin6.set_ga_par(Gsolv.ga)


if __name__ == '__main__':

    Gsolv.ga.evolve(freq_stats=10)
    print "Best individual found was" ,Gsolv.ga.bestIndividual().getRawScore()
