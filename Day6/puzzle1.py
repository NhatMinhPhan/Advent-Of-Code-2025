READ_FILE: str = 'example.txt'
numbers: list[list[int]] = []
operators: list[str] = []
results: list[int] = []

def multiply(operands: list[int]) -> int:
    product: int = 1
    for i in operands:
        assert isinstance(i, int), f"i ({i}) is not an int"
        product *= i
    return product

# File input
with open(READ_FILE, 'r') as file:
    while True:
        line = file.readline()
        if not line: # End of file
            break

        split: list[str] = line.strip().split(' ')
        split_2 = [item.strip() for item in split]
        
        while '' in split_2:
            split_2.remove('')

        if split_2[0].isdigit():
            numbers.append([int(item) for item in split_2])
        else:
            operators = split_2

for n in range(len(operators)):
    operands: list[int] = [numbers[i][n] for i in range(len(numbers))]
    match operators[n]:
        case '*':
            results.append(multiply(operands))
        case '+':
            results.append(sum(operands))
print(sum(results))