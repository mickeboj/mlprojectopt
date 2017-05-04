from solvers import GA
from functions import step


Gsolv = GA.Genetic_Solver()
Gsolv.set_fun(step.obj_fun,20)
step.set_genome_par(Gsolv.genome,step.get_bounds())
Gsolv.set_instance()
step.set_ga_par(Gsolv.ga)


if __name__ == '__main__':

    Gsolv.ga.evolve(freq_stats=10)
    print "Best individual found was" ,Gsolv.ga.bestIndividual().getRawScore()
