import numpy as np

class STest(object):

    def __init__(self,GAsolver,NSolver,bounds,num_runs):
        self.GAsolver = GAsolver
        self.NSolver = NSolver
        self.result = {}
        self.num_runs = num_runs
        self.bounds = bounds
    def run(self):
        print "Starting GA test"
        result = []
        for i in range(self.num_runs):
            result.append(self.GAsolver().solve())
            print "Test number %d (%d) done" %(i+1,self.num_runs)
        self.result['GARes'] = np.array(result)
        print "Starting N test"
        result = []
        for i in range(self.num_runs):
            result.append(self.NSolver.solve(self.bounds))
            print "Test number %d (%d) done" %(i+1,self.num_runs)
        self.result['NRes'] = np.array(result)

    def print_res(self):
        print "Result from running %d runs in terms of mean and std of the best solutions found" %self.num_runs
        print "%tGA Result: %1.3f (avg) %1.3f (std)"%(np.mean(self.result['GARes']),np.std(self.result['GARes']))
        print "%tGA Result: %1.3f (avg) %1.3f (std)"%(np.mean(self.result['NRes']),np.std(self.result['NRes']))
