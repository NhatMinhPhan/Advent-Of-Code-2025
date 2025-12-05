READ_FILE = 'example.txt'
grid: list[str] = []
accessible_rolls: set[tuple[int, int]] = set()

def roll_is_accessible(i: int, j: int, accessible_rolls: set[tuple[int, int]]) -> bool:
    '''
    Determine if a roll of paper can be accessed by a forklift.
    A roll of paper can be accessed by a forklift if there are
    fewer than four rolls of paper in the eight adjacent positions.
    If it is accessible, append (i, j) to accessible_roles and return True.
    Otherwise, return False.
    
    :param i: Row index
    :type i: int
    :param j: Column index
    :type j: int
    :param accessible_rolls: Set of coordinates where accessible rolls of paper can be found
    :type accessible_rolls: set[tuple[int, int]]
    :return: True if the roll of paper is accessible. False otherwise.
    :rtype: bool
    '''
    assert type(accessible_rolls) == set, 'accessible_roles is not a set'
    adjacent_squares: set[tuple[int, int]] = set()

    if i - 1 >= 0:
        if j - 1 >= 0: # Top left
            adjacent_squares.add((i - 1, j - 1))
        if j + 1 < len(grid[i]): # Top right
            adjacent_squares.add((i - 1, j + 1))
        adjacent_squares.add((i - 1, j)) # Top middle
    if i + 1 < len(grid):
        if j - 1 >= 0: # Bottom left
            adjacent_squares.add((i + 1, j - 1))
        if j + 1 < len(grid[i]): # Bottom right
            adjacent_squares.add((i + 1, j + 1))
        adjacent_squares.add((i + 1, j)) # Bottom middle
    if j - 1 >= 0: # Middle left
        adjacent_squares.add((i, j - 1))
    if j + 1 < len(grid[i]): # Middle right
        adjacent_squares.add((i, j + 1))
    
    roll_count: int = 0
    for square in adjacent_squares:
        roll_count = roll_count + 1 if grid[square[0]][square[1]] == '@' else roll_count
    
    if roll_count < 4:
        accessible_rolls.add((i, j))
        return True
    return False

# File input
with open(READ_FILE, 'r') as file:
    while True:
        line = file.readline()
        if not line: # End of file
            break
        grid.append(line.strip())

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            roll_is_accessible(i, j, accessible_rolls)

print(len(accessible_rolls))