from __future__ import print_function

# from sypo.chromosome import Chromosome
import sypo

if __name__ == '__main__':
    
    c = sypo.Chromosome(15)
    c.random()

    print(c)
    print(c.decode())
