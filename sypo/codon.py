from __future__ import print_function

import random

class Codon(object):

    def __init__(self):
        self.codon = [];
        self.codonlen = 3
        self.nucleotides = ['A', 'C', 'G', 'U']

    def __str__(self):

        return str(self.codon)

    def random(self):

        self.codon = [self.nucleotides[random.randint(0, 3)] for k in range(self.codonlen)]


def main():

    chromosome = []

    for k in range(10):

        c = Codon()
        c.random()
        chromosome.append(c)


    for c in chromosome:
        print(c)


if __name__ == '__main__':
    main()
