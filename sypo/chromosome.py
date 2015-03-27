from __future__ import print_function

import random

codons = {
    'UUU': 'F',
    'UUC': 'F',
    'UUA': 'L',
    'UUG': 'L',
    'CUU': 'L',
    'CUC': 'L',
    'CUA': 'L',
    'CUG': 'L',
    'AUU': 'I',
    'AUC': 'I',
    'AUA': 'I',
    'AUG': 'M',
    'GUU': 'V',
    'GUC': 'V',
    'GUA': 'V',
    'GUG': 'V',
    'UCU': 'S',
    'UCC': 'S',
    'UCA': 'S',
    'UCG': 'S',
    'CCU': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'ACU': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'GCU': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'UAU': 'Y',
    'UAC': 'Y',
    'UAA': 'Stop',
    'UAG': 'Stop',
    'CAU': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'AAU': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'GAU': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'UGU': 'C',
    'UGC': 'C',
    'UGA': 'Stop',
    'UGG': 'W',
    'CGU': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'AGU': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GGU': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G'
}

aminoacids = {
    'F': ['Phe', 'Phenylalanine'],
    'L': ['Leu', 'Leucine'],
    'I': ['Ile', 'Isoleucine'],
    'M': ['Met', 'Methionine'],
    'V': ['Val', 'Valine'],
    'S': ['Ser', 'Serine'],
    'P': ['Pro', 'Proline'],
    'T': ['Thr', 'Threonine'],
    'A': ['Ala', 'Alanine'],
    'Y': ['Tyr', 'Tyrosine'],
    'H': ['His', 'Histidine'],
    'Q': ['Gln', 'Glutamine'],
    'N': ['Asn', 'Asparagin'],
    'K': ['Lys', 'Lisine'],
    'D': ['Asp', 'Aspartic Acid'],
    'E': ['Glu', 'Glutamic Acid'],
    'C': ['Cys', 'Cysteine'],
    'W': ['Trp', 'Tryptophan'],
    'R': ['Arg', 'Arginine'],
    'G': ['Gly', 'Glycine']
}

class Chromosome(object):

    def __init__(self, length):
        self.chromosome = []
        self.length = length

    def __str__(self):
        return str(self.chromosome)

    def random(self):
        self.chromosome = [random.choice(codons.keys()) for k in range(self.length)]

    def decode(self):

        return [codons[k] for k in self.chromosome]
