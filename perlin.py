from perlin_noise import PerlinNoise
from math import cos, pi
from random import randint


def diceroll(chance):
    roll = randint(1, 20)
    return roll >= chance


class Chunk:
    lendth = 5
    struct = "ccccc"
    chance = 8

    def render(self, h_map, x):
        for i in range(len(self.struct)):
            coord = x + i
            if self.struct[i] == 'c':
                pass
            elif self.struct[i] == ' ':
                h_map[coord] = 0
            elif self.struct(i) == 'm':
                ran = float("inf")
                for j in range(1, self.lendth - i):
                    if struct[j] == "m":
                        h_map[j + x] = 



class Pit(Chunk):
    def __init__(self):
        self.pit_size = randint(1, self.lendth)
        self.struct = " " * self.pit_size + "c" * (self.lendth - self.pit_size)
        self.chance = 4

class Arena(Chunk):
    def __init__(self):
        self.struct = "m" * self.lendth


noise = PerlinNoise(octaves=8)
min_v = -1
max_v = 1
height = int(input())
width = int(input())
h_map = list(map(lambda x: noise(x / 10), range(width)))
norm_map = list(map(lambda x: (x - min_v) / (max_v - min_v), h_map))


def cosine_interpol(a, b, x):
    f = (1 - cos(x * pi)) / 2
    return a * (1 - f) + b * f

smoothed_map = []
for i in range(len(norm_map) - 1):
    smoothed_map.extend([norm_map[i], cosine_interpol(norm_map[i], norm_map[i + 1], norm_map[i] - int(norm_map[i]))])

for y in range(height, 0, -1):
    row = ''
    for x in smoothed_map:
        if x * height >= y:
                row += '█'
        else:
             row += ' '  # Пробел для пустого пространства
    print(row)
