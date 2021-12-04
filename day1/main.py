def get_numbers_from_file(file_name):
    lst = []
    with open(file_name, 'r') as handle:
        lst = [int(line.strip()) for line in handle]
    return lst
    
def get_window_sum(numbers, last_index, window_size):
    return sum(numbers[last_index-window_size:last_index])

numbers = get_numbers_from_file('numbers.txt')

# Count number of increases
count = 0
for prev, curr in zip(numbers[:-1], numbers[1:]):
    if curr > prev:
        count += 1
print(count)

# Count number of window increases
count = 0
window_size = 3
last_window_sum = None
for i in range(window_size-1, len(numbers)):
    window_sum = get_window_sum(numbers, i, window_size)
    if last_window_sum is None:
        pass
    elif window_sum > last_window_sum:
        count += 1
    last_window_sum = window_sum
print(count)
