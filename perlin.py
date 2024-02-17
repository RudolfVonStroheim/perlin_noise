from perlin_noise import PerlinNoise
from math import cos, pi
from random import randint



class Chunk:
    lendth = 5
    struct = "ccccc"
    chance = 8
    label = 'empty'
    enemy = False

    def update(self):
        pass

    def render(self, h_map, x):
        for i in range(len(self.struct)):
            coord = x + i
            if self.struct[i] == 'c':
                pass
            elif self.struct[i] == ' ':
                h_map[coord] = 0
            elif self.struct[i] == 'm':
                ran = float("inf")
                for j in range(1, self.lendth - i):
                    if self.struct[j] == "m":
                        ran = min(h_map[x + j], ran)
                    else:
                        break
                for j in range(self.lendth - i):
                    h_map[j] = ran
        self.update()


class Pit(Chunk):
    def __init__(self):
        self.pit_size = randint(1, self.lendth)
        self.struct = " " * self.pit_size + "c" * (self.lendth - self.pit_size)
        self.chance = 15
        self.label = 'pit'

    def update(self):
        self.pit_size = randint(1, self.lendth)


class Arena(Chunk):
    def __init__(self):
        self.struct = "m" * self.lendth
        self.chance = 16
        self.enemy = True
        self.label = 'Arena'


class Generator:
    def __init__(self, height, width):
        self.noise = PerlinNoise(octaves=8)
        self.min_v = -1
        self.max_v = 1
        self.height = height
        self.width = width
        self.generate_land()
        self.chunk = Chunk()
        self.structs = [Pit(), Arena()]
        self.chunk_count = self.width // self.chunk.lendth
        self.enemy_coords = []
        self.set_structures()

    def diceroll(self, chance):
        roll = randint(1, 20)
        return roll >= chance

    def get_map(self):
        return self.h_map, self.enemy_coords

    def set_structures(self): 
        for i in range(self.chunk_count):
            struct = None
            for prob in self.structs:
                if self.diceroll(prob.chance):
                    struct = prob
                    break
            if not struct:
                struct = self.chunk
            print(struct.label)
            if struct.enemy:
                self.enemy_coords.append(i * self.chunk.lendth)
            struct.render(self.h_map, self.chunk.lendth * i)

    def generate_land(self):
        h_map = list(map(lambda x: self.noise(x / 10), range(self.width)))
        self.h_map = list(map(lambda x: (x - self.min_v) / (self.max_v - self.min_v), h_map))
        self.smooth()

    def cosine_interpol(self, a, b, x):
        f = (1 - cos(x * pi)) / 2
        return a * (1 - f) + b * f

    def smooth(self):
        smoothed_map = []
        for i in range(len(self.h_map) - 1):
            smoothed_map.extend([self.h_map[i], self.cosine_interpol(self.h_map[i], self.h_map[i + 1], self.h_map[i] - int(self.h_map[i]))])
        self.h_map = smoothed_map

    def render(self):
        for y in range(self.height, 0, -1):
            row = ''
            for x in self.h_map:
                if x * self.height >= y:
                    row += '█'
                else:
                     row += ' '  # Пробел для пустого пространства
            print(row)


gener = Generator(int(input()), int(input()))
gener.render()
print()
print(*gener.get_map())
