from solvers import GA,BFGS
from functions import step

dim = 20
freq = 20
Gsolv = GA.Genetic_Solver()
Gsolv.set_fun(step.obj_fun,dim,freq)
step.set_genome_par(Gsolv.genome,step.get_bounds())
Gsolv.set_instance()
step.set_ga_par(Gsolv.ga)

Bsolv = BFGS.BFGS()
Bsolv.set_dim(dim)
Bsolv.set_obj_fun(step.obj_fun)
Bsolv.set_opt(True)

if __name__ == '__main__':

    best = Gsolv.solve()
    print "Best individual found for GA was" ,best
    best2 = Bsolv.solve(step.get_bounds())
    print "Best solution found using BFGS was", best2
    
