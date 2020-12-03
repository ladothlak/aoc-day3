with open('input.txt') as f:
    read_data = list(f)

# Make pattern repeat a good number of times so we can search it
for line in range(len(read_data)):
    read_data[line] = read_data[line].strip('\n')*50

start_pos = read_data[0][0]

num_open = 0
num_tree = 0

# Search from the start position
for line in range(1, len(read_data)):
    try:
        feature_at_pos = read_data[line][line*3]
    except:
        print('Error encountered')

    if feature_at_pos == '#':
        num_tree = num_tree + 1

    else:
        num_open = num_open + 1

print(num_tree)
