import numpy as np
import time

class DTest(object):

    def __init__(self,GAsolver,NSolver,bounds,opt_val,name):
        self.GAsolver = GAsolver
        self.NSolver = NSolver
        self.result = {}
        self.bounds = bounds
        self.dim = [(d+1)*10 for d in range(20)]
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
