from perlin_noise import PerlinNoise


width = 60
noise = PerlinNoise(octaves=9)
carta = [noise(i / 10) for i in range(width)]
height = 50
min_val = -1
max_val = 1
print('a' * 10)
normalized = [(value - min_val) / (max_val - min_val) for value in carta]
smoothed_values = []
for i in range(len(normalized) - 1):
    smoothed_values.extend([normalized[i], (normalized[i] + normalized[i + 1]) / 2])
print(*normalized)
for y in range(height, 0, -1):
    row = ''
    for value in smoothed_values:
        if value * height >= y:
            row += '█'  # Символ для высоты столбца
        else:
            row += ' '  # Пробел для пустого пространства
    print(row)
