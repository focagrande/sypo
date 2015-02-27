from sypo.chromosome import Chromosome

import types

class TestSypo(object):

    def test_chromosome_instance(self):

        c = Chromosome(15)
        assert isinstance(c, Chromosome)

    def test_chromosome_length(self):

        c = Chromosome(15)
        c.random()
        assert len(c.chromosome) == 15

    def test_chromosome_decode(self):

        c = Chromosome(15)
        c.random()
        assert len(c.decode()) == 15

    def test_chromosome_str(self):

        c = Chromosome(15)
        c.random()

        assert type(c.__str__()) in types.StringTypes
