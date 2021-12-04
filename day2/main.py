from functools import reduce

def read_cmds(path):
    parse = lambda l: \
        (int(l[1]), 0) if l[0] == 'forward' else \
        (0, int(l[1]) if l[0] == 'down' else -int(l[1]))
    with open(path, 'r') as handle:
        return [parse(l.split()) for l in handle]

add_pair = lambda p1, p2: (p1[0]+p2[0], p1[1]+p2[1])

perform_instruction = lambda curr, cmd: \
        (curr[0]+cmd[0], curr[1] + curr[2]*cmd[0], curr[2] + cmd[1])

output_answer = lambda result: result[0] * result[1]

commands = read_cmds('input.txt')
print(output_answer(reduce(add_pair, commands))) # Part 1
print(output_answer(reduce(perform_instruction, [(0, 0, 0)] + commands))) # Part 2
