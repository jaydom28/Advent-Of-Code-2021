def read_lines(file_path):
    with open(file_path, 'r') as handle:
        return [line.strip() for line in handle]


def count_bits(numbers):
    counts = [0] * len(numbers[0])
    for num in numbers:
        for i, bit in enumerate(num):
            counts[i] += int(bit)

    return counts


lines = read_lines('test.txt')
counts = count_bits(lines)
total_lines = len(lines)

gamma = [int(c > total_lines/2) for c in counts]
epsilon = [int(not bit) for bit in gamma]
gamma = int(''.join(str(bit) for bit in gamma), 2)
epsilon = int(''.join(str(bit) for bit in epsilon), 2)

print(f'Part 1:\n  {gamma * epsilon}\n')

oxygen_rating = lines
co2_rating = lines

for i in range(len(oxygen_rating[0])):
    counts = count_bits(oxygen_rating)
    total = len(oxygen_rating)
    more_common_bit = int(counts[i] >= total/2)
    oxygen_rating = [num for num in oxygen_rating if int(num[i]) == more_common_bit]
    if len(oxygen_rating) == 1:
        break

for i in range(len(co2_rating[0])):
    counts = count_bits(co2_rating)
    total = len(co2_rating)
    more_common_bit = int(counts[i] >= total/2)
    co2_rating = [num for num in co2_rating if int(num[i]) != more_common_bit]
    if len(co2_rating) == 1:
        break

oxygen_rating = int(oxygen_rating[0], 2)
co2_rating = int(co2_rating[0], 2)

print('Part 2')
print(f'  Oxygen rating: {oxygen_rating}')
print(f'  CO2 rating: {co2_rating}')
print('  ' + str(oxygen_rating * co2_rating))
