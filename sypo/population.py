from __future__ import print_function

from .chromosome import Chromosome

class Population(object):

    def __init__(self, chromlen, popcount):

        self.population = []
        self.popcount = popcount
        self.chromlen = chromlen

    def populate(self):

        self.population = [Chromosome(self.chromlen) for k in range(self.popcount)]

        for c in self.population:
            c.random()
