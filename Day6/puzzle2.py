READ_FILE: str = 'example.txt'
operands: list[list[str]] = []
operators: list[str] = []
results: list[int] = []

lines: list[str] = []
nums_of_occupied_spaces: list[int] = []

def multiply(operands: list[int]) -> int:
    product: int = 1
    for i in operands:
        assert isinstance(i, int), f"i ({i}) is not an int"
        product *= i
    return product

def cephalopod_convert(cephalopod_operands: list[str]) -> list[int]:
    ''' Turn a list of cephalopod math operands (str) into a list of ordinary math operands (int) '''
    ordinary_operands: list[int] = []
    for j in range(len(cephalopod_operands[0])):
        operand_str: str = ''
        for i in range(len(cephalopod_operands)):
            operand_str += '' if cephalopod_operands[i][j] == ' ' else cephalopod_operands[i][j]
        ordinary_operands.append(int(operand_str))
    return ordinary_operands

def cephalopod_multiply(operands: list[str]) -> int:
    ordinary_operands = cephalopod_convert(operands)
    return multiply(ordinary_operands)

def cephalopod_sum(operands: list[str]) -> int:
    ordinary_operands = cephalopod_convert(operands)
    return sum(ordinary_operands)

# File input
with open(READ_FILE, 'r') as file:
    while True:
        line = file.readline()
        if not line: # End of file
            break
        # Append line to lines without newline at index -1 if there is a newline
        lines.append(line[:-1] if line[-1] == '\n' else line)


# The last item in lines is the one with the operators.
operators: list[str] = lines[-1].strip().split(' ')
operators = [item.strip() for item in operators]

while '' in operators:
    operators.remove('')

# Count the number of occupied spaces in between the operators
num_of_spaces: int = 0
for char in lines[-1]:
    if char != ' ':
        if num_of_spaces > 0:
            nums_of_occupied_spaces.append(num_of_spaces - 1) # - 1 to account for the space in between each problem
        num_of_spaces = 0
    num_of_spaces += 1
# At the end of lines[-1], append to include the final column, now without a space following it
nums_of_occupied_spaces.append(num_of_spaces)

# Process the previous items (for the operands)
for n in range(len(lines) - 1): # len(lines) - 1 so as to avoid the last line which stores operators
    operands.append([])
    operand_list = operands[-1]
    current_line = lines[n]
    line_index: int = 0
    column_index: int = 0
    while line_index < len(current_line) and column_index < len(nums_of_occupied_spaces):
        operand_list.append(current_line[line_index : line_index + nums_of_occupied_spaces[column_index]])
        line_index += nums_of_occupied_spaces[column_index] + 1 # + 1 to account for the separating space in between columns
        column_index += 1

for n in range(-1, -len(operators) - 1, -1):
    operand_strs: list[str] = [operands[i][n] for i in range(len(operands))]
    match operators[n]:
        case '*':
            results.append(cephalopod_multiply(operand_strs))
        case '+':
            results.append(cephalopod_sum(operand_strs))
print(sum(results))