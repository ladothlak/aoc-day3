import math

with open('input.txt') as f:
    read_data = list(f)

# Make pattern repeat a good number of times so we can search it
for line in range(len(read_data)):
    read_data[line] = read_data[line].strip('\n')*500

start_pos = read_data[0][0]

patterns = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
iteration = 0

tree_count = [0]*len(patterns)

# Search from the start position
for pattern in patterns:
    tree_count[iteration] = 0
    right = patterns[iteration][0]
    down = patterns[iteration][1]

    for line in range(1, int(len(read_data)/down)):
        try:
            feature_at_pos = read_data[line*down][line*right]
        except:
            print('Error encountered')

        if feature_at_pos == '#':
            tree_count[iteration] = tree_count[iteration] + 1

    iteration = iteration + 1

print(math.prod(tree_count))
