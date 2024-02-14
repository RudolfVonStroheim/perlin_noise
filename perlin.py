from math import cos, pi
from random import random, seed

with open("primes.txt") as f:
    PRIME = int(f.read())


class PerlinGenerator:
    def __init__(self, lendth, oct_num, pers):
        self.lendth = lendth
        self.oct_num = oct_num
        self.pers = pers

    def noise(self, x):
        seed(x)
        return random()


    def interp(self, a, b, x):
        ft = x * pi
        f = (1-cos(ft))/2
        return a*(1 - f) + b * f


    def smoothed_noise(self, x):
        noise = self.noise
        return noise(x) / 2+noise(x - 1) / 4 + noise(x + 1) / 4


    def interpolated_noise(self, x):
        smoothed_noise = self.smoothed_noise
        interp = self.interp
        integer_X = int(x)
        fractional_X = x - integer_X
        v1 = smoothed_noise(integer_X)
        v2 = smoothed_noise(integer_X + 1)
        return interp(v1, v2, fractional_X)


    def perlin_noise(self, x):
        total = 0
        pers = self.pers
        for i in range(self.oct_num):
            freq = 2 * i
            amp = pers * i
