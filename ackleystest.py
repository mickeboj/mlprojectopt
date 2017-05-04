from solvers import GA,BFGS
from functions import ackley

dim = 20

Gsolv = GA.Genetic_Solver()
Gsolv.set_fun(ackley.obj_fun,dim,100)
ackley.set_genome_par(Gsolv.genome,ackley.get_bounds())
Gsolv.set_instance()
ackley.set_ga_par(Gsolv.ga)

Bsolv = BFGS.BFGS()
Bsolv.set_dim(dim)
Bsolv.set_obj_fun(ackley.obj_fun)
Bsolv.set_opt(True)



if __name__ == '__main__':

    best = Gsolv.solve()
    print "Best individual found for GA was" ,best
    best2 = Bsolv.solve(ackley.get_bounds())
    print "Best solution found was", best2
