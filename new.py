from noise import pnoise1
from random import choice


class Map:
    def __init__(self, lendth) :
        self.lendth = lendth
        self.chunk_size = 5
        self.octaves = 8
        self.span = 5.0
        self.generate()

    def __iter__(self):
        return iter(self.map)

    def __getelem__(self, ind):
        return self.map[ind]

    def __len__(self):
        return self.lendth

    def __next__(self):
        return next(self.map)

    def generate(self):
        self.generate_relief()
        pass

    def generate_relief(self):
        self.map = 
