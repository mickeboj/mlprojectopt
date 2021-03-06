import numpy as np
import time
import matplotlib.pyplot as plt

class TTest(object):

    def __init__(self,GAsolver,NSolver,bounds,dim,num_runs,name):
        self.GAsolver = GAsolver
        self.NSolver = NSolver
        self.result = {}
        self.num_runs = num_runs
        self.bounds = bounds
        self.dim = dim
        self.fun_name = name
    def run(self):
        print "\n\t\t-------- Time Test --------\n"
        print "\nStarting GA test"
        result = []
        for i in range(self.num_runs):
            start = time.time()
            self.GAsolver(self.dim).solve()
            end = time.time()
            result.append(end-start)
            print "Test number %d (%d) done" %(i+1,self.num_runs)
        self.result['GARes'] = np.array(result)
        print "\nStarting %s test" %self.NSolver.name()
        result = []
        for i in range(self.num_runs):
            start = time.time()
            self.NSolver.solve(self.bounds)
            end = time.time()
            result.append(end-start)
            print "Test number %d (%d) done" %(i+1,self.num_runs)
        self.result['NRes'] = np.array(result)

    def print_res(self):
        print "\n\n\t\t-------- Result from testing %s over %d runs in terms of time taken--------\n\n" %(self.fun_name,self.num_runs)
        print "\tGA Time result: %1.3fs (avg) %1.3fs (std)"%(np.mean(self.result['GARes']),np.std(self.result['GARes']))
        print "\t%s Time result: %1.3fs (avg) %1.3fs (std)"%(self.NSolver.name(),np.mean(self.result['NRes']),np.std(self.result['NRes']))

    def plot_res(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        GA_line = ax.plot(np.array(range(self.num_runs)),self.result['GARes'],label="Genetic Algorithm")
        N_line = ax.plot(np.array(range(self.num_runs)),self.result['NRes'],label=self.NSolver.name())
        ax.legend()
        ax.set_xlabel('Run #')
        ax.set_ylabel('Time (s)')
        ax.set_title("Computational time for %s (%d dimensions)" %(self.fun_name,self.dim))
        plt.show()
