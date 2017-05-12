import numpy as np

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
        print "Starting GA test"
        result = []
        for i in range(self.num_runs):
            result.append(np.abs(self.GAsolver(self.dim).solve()-self.opt_val))
            print "Test number %d (%d) done" %(i+1,self.num_runs)
        self.result['GARes'] = np.array(result)
        print "Starting %s test" %self.NSolver.name()
        result = []
        for i in range(self.num_runs):
            result.append(np.abs(self.NSolver.solve(self.bounds)-self.opt_val))
            print "Test number %d (%d) done" %(i+1,self.num_runs)
        self.result['NRes'] = np.array(result)

    def print_res(self):
        print "Result from testing %s %d runs comparing the best solution found with the optimal one.\n The difference is then sumed up over the 10 runs" %(self.fun_name,self.num_runs)
        print "\tGA Result: %1.3f (avg) %1.3f (std)"%(np.mean(self.result['GARes']),np.std(self.result['GARes']))
        print "\t%s Result: %1.3f (avg) %1.3f (std)"%(self.NSolver.name(),np.mean(self.result['NRes']),np.std(self.result['NRes']))
