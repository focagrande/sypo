from __future__ import print_function

from sypo import Chromosome

if __name__ == '__main__':
    
    c = Chromosome(15)
    c.random()

    print(c)
    print(c.decode())
