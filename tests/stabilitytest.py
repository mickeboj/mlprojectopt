import numpy as np
import matplotlib.pyplot as plt


class STest(object):

    def __init__(self,GAsolver,NSolver,bounds,dim,num_runs,name):
        self.GAsolver = GAsolver
        self.NSolver = NSolver
        self.result = {}
        self.num_runs = num_runs
        self.bounds = bounds
        self.dim = dim
        self.fun_name = name
        self.tol = 2.5

    def run(self):
        print "\n\t\t-------- Stability Test --------\n"
        print "\nStarting GA test"
        result = []
        for i in range(self.num_runs):
            result.append(self.GAsolver(self.dim).solve())
            print "Test number %d (%d) done" %(i+1,self.num_runs)
        self.result['GARes'] = np.array(result)
        print "\nStarting %s test" %self.NSolver.name()
        result = []
        for i in range(self.num_runs):
            result.append(self.NSolver.solve(self.bounds))
            print "Test number %d (%d) done" %(i+1,self.num_runs)
        self.result['NRes'] = np.array(result)
        medR = np.median(self.result['NRes'])
        self.result['NResC'] = (len(self.result['NRes'][np.where(abs(self.result['NRes']-medR)<=self.tol)])+0.0)/self.num_runs
        medG = np.median(self.result['GARes'])
        self.result['GAResC'] = (len(self.result['GARes'][np.where(abs(self.result['GARes']-medG)<=self.tol)])+0.0)/self.num_runs

    def print_res(self):
        print "\n\n\t\t-------- Result from testing %s over %d runs in terms of how many times the best solution was within the tolerance (%1.2f)--------\n" %(self.fun_name,self.num_runs,self.tol)
        print "\tGA Result: %1.2f of the solutions was within the tolerance"%self.result['GAResC']
        print "\t%s Result: %1.2f of the solutions was within the tolerance"%(self.NSolver.name(),self.result['NResC'])

    def plot_res(self):

        fig = plt.figure()
        ax = fig.add_subplot(111)

        labels = ['"Genetic Algorithm"',self.NSolver.name()]

        bplot = ax.boxplot([self.result['GARes'],self.result['NRes']], patch_artist=True, labels = labels)
        colors = ['lightblue', 'lightgreen']

        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

        ax.set_xlabel('Solver')
        ax.set_yticks([])
        ax.set_ylabel('Difference in best solution')
        ax.set_title("Difference in best solution for %s (%d dimensions)" %(self.fun_name,self.dim))

        plt.show()
