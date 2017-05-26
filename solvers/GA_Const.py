from pyevolve import G1DList, GSimpleGA, Selectors
from pyevolve import Initializators, Mutators, Consts, Util
import math
import random
import logging
from time import time
from types import BooleanType
from sys import platform as sys_platform
from sys import stdout as sys_stdout
import code
from pyevolve.GPopulation import GPopulation
from pyevolve.FunctionSlot import FunctionSlot
from pyevolve.GenomeBase import GenomeBase
from pyevolve.DBAdapters import DBBaseAdapter
import pyevolve
import numpy as np


class GConstGA(GSimpleGA.GSimpleGA):

    def __init__(self,genome,check_fun):
        super(GConstGA,self).__init__(genome)
        self.check_fun  = check_fun


    def step(self):
        """ Just do one step in evolution, one generation """
        newPop = GPopulation(self.internalPop)
        logging.debug("Population was cloned.")

        size_iterate = len(self.internalPop)

        # Odd population size
        if size_iterate % 2 != 0:
            size_iterate -= 1

        crossover_empty = self.select(popID=self.currentGeneration).crossover.isEmpty()

        for i in xrange(0, size_iterate, 2):
            while True:
                genomeMom = self.select(popID=self.currentGeneration)
                genomeDad = self.select(popID=self.currentGeneration)

                if not crossover_empty and self.pCrossover >= 1.0:
                    for it in genomeMom.crossover.applyFunctions(mom=genomeMom, dad=genomeDad, count=2):
                        (sister, brother) = it
                else:
                    if not crossover_empty and Util.randomFlipCoin(self.pCrossover):
                        for it in genomeMom.crossover.applyFunctions(mom=genomeMom, dad=genomeDad, count=2):
                            (sister, brother) = it
                    else:
                        sister = genomeMom.clone()
                        brother = genomeDad.clone()

                sister.mutate(pmut=self.pMutation, ga_engine=self)
                brother.mutate(pmut=self.pMutation, ga_engine=self)
                if self.check_fun(np.array(sister.genomeList)) and self.check_fun(np.array(brother.genomeList)):
                    break

            newPop.internalPop.append(sister)
            newPop.internalPop.append(brother)

        if len(self.internalPop) % 2 != 0:
            while True:
                genomeMom = self.select(popID=self.currentGeneration)
                genomeDad = self.select(popID=self.currentGeneration)

                if Util.randomFlipCoin(self.pCrossover):
                    for it in genomeMom.crossover.applyFunctions(mom=genomeMom, dad=genomeDad, count=1):
                        (sister, brother) = it
                else:
                    sister = random.choice([genomeMom, genomeDad])
                    sister = sister.clone()
                    sister.mutate(pmut=self.pMutation, ga_engine=self)

                if self.check_fun(np.array(sister.genomeList)):
                    break
            newPop.internalPop.append(sister)

        logging.debug("Evaluating the new created population.")
        newPop.evaluate()

        if self.elitism:
            logging.debug("Doing elitism.")
            if self.getMinimax() == Consts.minimaxType["maximize"]:
                for i in xrange(self.nElitismReplacement):
                    #re-evaluate before being sure this is the best
                    self.internalPop.bestRaw(i).evaluate()
                    if self.internalPop.bestRaw(i).score > newPop.bestRaw(i).score:
                        newPop[len(newPop) - 1 - i] = self.internalPop.bestRaw(i)
            elif self.getMinimax() == Consts.minimaxType["minimize"]:
                for i in xrange(self.nElitismReplacement):
                    #re-evaluate before being sure this is the best
                    self.internalPop.bestRaw(i).evaluate()
                    if self.internalPop.bestRaw(i).score < newPop.bestRaw(i).score:
                        newPop[len(newPop) - 1 - i] = self.internalPop.bestRaw(i)

        self.internalPop = newPop
        self.internalPop.sort()

        logging.debug("The generation %d was finished.", self.currentGeneration)

        self.currentGeneration += 1

        if self.max_time:
           total_time = time() - self.time_init
           if total_time > self.max_time:
              return True
        return self.currentGeneration == self.nGenerations





class Genetic_Solver(object):


    def __init__(self):
        self.genome = None
        self.ga = None
        self.freq = None

    def set_fun(self,fun,dim,freq):
        self.genome = G1DList.G1DList(dim)
        self.genome.evaluator.set(fun)
        self.freq = freq

    def set_instance(self):
        self.ga = GConstGA(self.genome)
        self.ga.minimax = Consts.minimaxType["minimize"]

    def solve(self):
        self.ga.evolve(freq_stats=self.freq)
        return self.ga.bestIndividual().getRawScore()
