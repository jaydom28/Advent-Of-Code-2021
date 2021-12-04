from collections import Counter


class Tile:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        self.marked = False

    def __repr__(self):
        return f'({self.number}, {self.x}, {self.y}, marked={self.marked})'


class Board:
    def __init__(self, tiles):
        self.tiles = tiles
        self.total_tiles = 25
        self.num_marked = 0

        # Keep track of the number of tiles that have certain x,y vals to check
        # for winner
        self.x_counts = Counter()
        self.y_counts = Counter()

    @classmethod
    def from_array(cls, array):
        tiles_array = []
        for i, row in enumerate(array, 1):
            tiles_array.append([])
            for j, num in enumerate(row, 1):
                new_tile = Tile(num, i, j)
                tiles_array[i-1].append(new_tile)

        return cls(tiles_array)

    def get_tiles(self):
        return list(t for row in self.tiles
                    for t in row)

    def check_for_number(self, number):
        tile = next((t for row in self.tiles
                     for t in row if t.number == number), None)
        if tile is None or tile.marked:
            return

        tile.marked = True
        self.y_counts[tile.y] += 1
        self.x_counts[tile.x] += 1

    def is_winner(self):
        return any(y == 5 for y in self.y_counts.values()) or \
               any(x == 5 for x in self.x_counts.values())


def get_data(file_path):
    with open(file_path, 'r') as handle:
        lines = handle.readlines()
    numbers = [int(num) for num in lines[0].strip().split(',')]

    tiles, boards = [], []
    for line in lines[2:]:
        if line == '\n':
            boards.append(Board.from_array(tiles))
            tiles.clear()
            continue
        tiles.append([int(num) for num in line.split()])
    boards.append(Board.from_array(tiles))

    return numbers, boards


nums, boards = get_data('input.txt')
for num in nums:
    _ = [b.check_for_number(num) for b in boards]
    winning_board = next((b for b in boards if b.is_winner()), None)
    if winning_board is not None:
        print("WE HAVE A WINNER")
        break

unmarked_sum = sum(t.number for t in winning_board.get_tiles() if not t.marked)
print(f'Part 1: {unmarked_sum * num}')

nums, boards = get_data('input.txt')
winning_boards = []

for num in nums:
    for board in [b for b in boards if b not in winning_boards]:
        board.check_for_number(num)
        if board.is_winner():
            winning_boards.append(board)
    if len(winning_boards) == len(boards):
        break

winning_board = winning_boards[-1]
unmarked_sum = sum(t.number for t in winning_board.get_tiles() if not t.marked)
print(f'Part 2: {unmarked_sum * num}')
