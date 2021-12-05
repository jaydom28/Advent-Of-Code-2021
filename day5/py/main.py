from collections import Counter


def read_coords(file_path):
    coord_pairs = []
    with open(file_path, 'r') as handle:
        for line in handle:
            coord1, coord2 = line.split('->')
            coord1 = tuple(int(n) for n in coord1.split(','))
            coord2 = tuple(int(n) for n in coord2.split(','))
            coord_pairs.append((coord1, coord2))
            print(coord1, coord2)
    return coord_pairs


def expand_pair(a, b, diagonal=False):
    output = []

    if not diagonal and a[0] != b[0] and a[1] != b[1]:
        return []

    x, y = a
    dx = 0 if a[0] == b[0] else 1 if a[0] < b[0] else -1
    dy = 0 if a[1] == b[1] else 1 if a[1] < b[1] else -1

    while x != b[0] or y != b[1]:
        output.append((x, y))
        x += dx
        y += dy

    output.append((x, y))
    return output


coords = read_coords('../input.txt')
grid = Counter()
for a, b in coords:
    for coord in expand_pair(a, b):
        grid[coord] += 1

part1 = sum(1 for count in grid.values() if count >= 2)
print(f'Part1: {part1}')

grid.clear()
for a, b in coords:
    for coord in expand_pair(a, b, diagonal=True):
        grid[coord] += 1

part2 = sum(1 for count in grid.values() if count >= 2)
print(f'Part2: {part2}')
