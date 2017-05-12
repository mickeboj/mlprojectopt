import numpy as np
import time
import matplotlib.pyplot as plt

class DTest(object):

    def __init__(self,GAsolver,NSolver,bounds,dim,opt_val,name):
        self.GAsolver = GAsolver
        self.NSolver = NSolver
        self.result = {}
        self.bounds = bounds
        self.dim = dim
        self.opt_val = opt_val
        self.fun_name = name

    def run(self):
        print "\n\t\t-------- Dimension Test --------\n"
        print "\nStarting GA test"
        result_err = []
        result_time = []
        for i in range(len(self.dim)):
            start = time.time()
            result_err.append(np.abs(self.GAsolver(self.dim[i]).solve()-self.opt_val))
            end = time.time()
            result_time.append(end-start)
            print "Test number %d (%d) done" %(i+1,len(self.dim))
        self.result['GAResE'] = np.array(result_err)
        self.result['GAResT'] = np.array(result_time)
        print "\nStarting %s test" %self.NSolver.name()
        result_err = []
        result_time = []
        for i in range(len(self.dim)):
            start = time.time()
            self.NSolver.set_dim(self.dim[i])
            result_err.append(np.abs(self.NSolver.solve(self.bounds)-self.opt_val))
            end = time.time()
            result_time.append(end-start)
            print "Test number %d (%d) done" %(i+1,len(self.dim))
        self.result['NResE'] = np.array(result_err)
        self.result['NResT'] = np.array(result_time)

    def print_res(self):
        print "\n\n\t\t--------Result from testing %s over %d different dimensions with both time and error   --------\n" %(self.fun_name,len(self.dim))
        print "\tGA Error Result: %1.3f (avg) %1.3f (std)"%(np.mean(self.result['GAResE']),np.std(self.result['GAResE']))
        print "\t%s Error Result: %1.3f (avg) %1.3f (std)"%(self.NSolver.name(),np.mean(self.result['NResE']),np.std(self.result['NResE']))
        print "\tGA Time Result: %1.3f (avg) %1.3f (std)"%(np.mean(self.result['GAResT']),np.std(self.result['GAResT']))
        print "\t%s Time Result: %1.3f (avg) %1.3f (std)"%(self.NSolver.name(),np.mean(self.result['NResT']),np.std(self.result['NResT']))

    def plot_res(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(211)
        GA_line1 = ax1.plot(np.array(self.dim),self.result['GAResE'],label="Genetic Algorithm")
        N_line1 = ax1.plot(np.array(self.dim),self.result['NResE'],label=self.NSolver.name())
        ax1.legend()
        ax1.set_xlabel('Dimensions')
        ax1.set_ylabel('Error')
        ax1.set_title("Error over dimensions %s"%self.fun_name)
        ax2 = fig.add_subplot(212)
        GA_line2 = ax2.plot(np.array(self.dim),self.result['GAResT'],label="Genetic Algorithm")
        N_line2 = ax2.plot(np.array(self.dim),self.result['NResT'],label=self.NSolver.name())
        ax2.legend()
        ax2.set_xlabel('Dimensions')
        ax2.set_ylabel('Time (s)')
        ax2.set_title("Computational time over dimensions %s"%self.fun_name)
        plt.show()
