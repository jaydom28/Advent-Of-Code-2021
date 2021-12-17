import math

def read_input(file_path):
    with open(file_path, 'r') as handle:
        file_lines = [line.strip() for line in handle]

    symbol_mapping = {}
    for line in file_lines[2:]:
        combo, result = line.split(' -> ')
        symbol_mapping[combo] = result
    return (file_lines[0], symbol_mapping)

def dictify_string(input_string):
    output = {}
    for i in range(len(input_string)-1):
        key = input_string[i:i+2]
        output[key] = output.get(key, 0) + 1
    return output

def apply_step(start, mappings):
    print(start)
    output = {}

    for letter_pair, letter_pair_count in start.items():
        fst, snd = letter_pair
        new_letter = mappings[letter_pair]
        # print(f'{letter_pair} -> {letter_pair_count}')
        # print(f'{letter_pair} -> {new_letter}')
        output[fst+new_letter] = output.get(fst+new_letter, 0) + letter_pair_count
        # print(f'New Count: {fst+new_letter} -> {output[fst+new_letter]}')
        output[new_letter+snd] = output.get(new_letter+snd, 0) + letter_pair_count
        # print(f'New Count: {new_letter+snd} -> {output[new_letter+snd]}')

    print(output)
    return output

def count_letters(template):
    output = {}
    for letter_pair, letter_pair_count in template.items():
        fst, snd = letter_pair
        output[fst] = output.get(fst, 0) + letter_pair_count
        output[snd] = output.get(snd, 0) + letter_pair_count
    return {k: math.ceil(v/2) for (k, v) in output.items()}

print('hello world!')
input_file = '../input.txt'
template, symbol_mappings = read_input(input_file)
print(template)
template = dictify_string(template)

for _ in range(10):
    template = apply_step(template, symbol_mappings)
    print(count_letters(template))
    print('~'*10)

letter_counts = count_letters(template)
least_common = min(letter_counts.items(), key=lambda x: x[1])
most_common = max(letter_counts.items(), key=lambda x: x[1])
print(f'Part 1: {most_common[1]-least_common[1]}')

for _ in range(30):
    template = apply_step(template, symbol_mappings)
    print(count_letters(template))
    print('~'*10)

template = count_letters(template)
least_common = min(template.items(), key=lambda x: x[1])
most_common = max(template.items(), key=lambda x: x[1])
print(f'Part 2: {most_common[1]-least_common[1]}')
