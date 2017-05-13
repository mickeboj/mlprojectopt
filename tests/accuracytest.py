import numpy as np
import matplotlib.pyplot as plt

class ATest(object):

    def __init__(self,GAsolver,NSolver,bounds,dim,num_runs,opt_val,name):
        self.GAsolver = GAsolver
        self.NSolver = NSolver
        self.result = {}
        self.num_runs = num_runs
        self.bounds = bounds
        self.dim = dim
        self.opt_val = opt_val
        self.fun_name = name

    def run(self):
        print "\n\t\t-------- Accuracy Test --------\n"
        print "\nStarting GA test"
        result = []
        for i in range(self.num_runs):
            result.append(np.abs(self.GAsolver(self.dim).solve()-self.opt_val))
            print "Test number %d (%d) done" %(i+1,self.num_runs)
        self.result['GARes'] = np.array(result)
        print "\nStarting %s test" %self.NSolver.name()
        result = []
        for i in range(self.num_runs):
            result.append(np.abs(self.NSolver.solve(self.bounds)-self.opt_val))
            print "Test number %d (%d) done" %(i+1,self.num_runs)
        self.result['NRes'] = np.array(result)

    def print_res(self):
        print "\n\n\t\t--------Result from testing %s %d runs comparing the best solution found with the optimal one --------\n"%(self.fun_name,self.num_runs)
        print "The result is stored as an absolute error relative to the optimal one (%1.1f)\n" %self.opt_val
        print "\tGA Result: %1.3f (avg) %1.3f (std)"%(np.mean(self.result['GARes']),np.std(self.result['GARes']))
        print "\t%s Result: %1.3f (avg) %1.3f (std)"%(self.NSolver.name(),np.mean(self.result['NRes']),np.std(self.result['NRes']))

    def plot_res(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        GA_line = ax.plot(np.array(range(self.num_runs)),self.result['GARes'],label="Genetic Algorithm")
        N_line = ax.plot(np.array(range(self.num_runs)),self.result['NRes'],label=self.NSolver.name())
        ax.legend()
        ax.set_xlabel('Run #')
        ax.set_ylabel('Error')
        ax.set_title("Absolte error for %s (%d dimensions)" %(self.fun_name,self.dim))
        plt.show()
