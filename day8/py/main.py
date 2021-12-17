class Decoder:
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.e = None
        self.f = None
        self.g = None


def parse_line(line):
    mixed, output = line.split('|')
    mixed = [set(sig) for sig in mixed.strip().split()]
    output = [set(sig) for sig in output.strip().split()]
    return mixed, output


def read_lines(file_path):
    output = []
    with open(file_path, 'r') as handle:
        for line in handle:
            output.append(parse_line(line))
    return output


def decipher(mixed_signals):
    one = next(s for s in mixed_signals if len(s) == 2)
    mixed_signals.remove(one)
    print(f'The signal representing one is: {one}')

    seven = next(s for s in mixed_signals if len(s) == 3)
    mixed_signals.remove(seven)
    print(f'The signal representing seven is: {seven}')

    four = next(s for s in mixed_signals if len(s) == 4)
    mixed_signals.remove(four)
    print(f'The signal representing four is: {four}')

    eight = next(s for s in mixed_signals if len(s) == 7)
    mixed_signals.remove(eight)
    print(f'The signal representing eight is: {eight}')

    zero = next(s for s in mixed_signals if len(s) == 6 and not four.issubset(s) and s.issubset(eight))
    mixed_signals.remove(zero)
    print(f'The signal representing zero is: {zero}')

    nine = next(s for s in mixed_signals if len(s) == 6 and s.issubset(eight) and not s.issubset(zero))
    mixed_signals.remove(nine)
    print(f'The signal representing nine is: {nine}')

    six = next(s for s in mixed_signals if len(s) == 6 and not seven.issubset(s) and s.issubset(eight))
    print(f'The signal representing six is: {six}')

    five = next(s for s in mixed_signals if len(s) == 5 and s.issubset(six) and s.issubset(eight))
    print(f'The signal representing five is: {five}')

    return one


signals = read_lines('../test.txt')
for mix, out in signals:
    print(f'mixed: {mix}')
    decipher(mix)
    break
    print(f'output: {out}')

part1 = 0
for _, output in signals:
    print(output[0])
    part1 += sum(1 for sig in output if len(sig) in [2, 3, 4, 7])
print(f'Part 1: {part1}')
