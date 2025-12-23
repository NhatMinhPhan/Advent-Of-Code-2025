READ_FILE = 'example.txt'
grid: list[str] = []

# File input
with open(READ_FILE, 'r') as file:
    while True:
        line = file.readline()
        if not line: # End of file
            break
        grid.append(line.strip())

beam_pos_set: set[int] = set()
split_times: int = 0

# Find the position of S in grid[0]. That will be the position of the 1st tachyon beam.
beam_pos_set.add(grid[0].find('S'))

# Traverse through the rest of the grid.
for row in grid:
    for pos in range(len(row)):
        if row[pos] == '^' and pos in beam_pos_set: # If a beam is about to hit this ^
            # Split the beam
            beam_pos_set.remove(pos)
            if pos - 1 >= 0:
                beam_pos_set.add(pos - 1)
            if pos + 1 < len(row):
                beam_pos_set.add(pos + 1)
            split_times += 1
            pass

print(split_times)