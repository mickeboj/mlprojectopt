from solvers import GA
from functions import ackley


Gsolv = GA.Genetic_Solver()
Gsolv.set_fun(ackley.obj_fun,20)
ackley.set_genome_par(Gsolv.genome,ackley.get_bounds())
Gsolv.set_instance()
ackley.set_ga_par(Gsolv.ga)


if __name__ == '__main__':

    Gsolv.ga.evolve(freq_stats=100)
    print "Best individual found was" ,Gsolv.ga.bestIndividual().getRawScore()
