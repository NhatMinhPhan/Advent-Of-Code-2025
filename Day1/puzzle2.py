READ_FILE = 'example.txt'
dial: int = 50
zero_count = 0

def rotate_dial(line: str, dial: int, zero_count: int) -> tuple[int, int]:
    amount: int = int(line[1:])
    match line[0]:
        case 'L':
            for i in range(amount):
                dial -= 1
                if dial % 100 == 0:
                    zero_count += 1
            pass
        case 'R':
            for i in range(amount):
                dial += 1
                if dial % 100 == 0:
                    zero_count += 1
            pass
    return dial, zero_count

# File input
with open(READ_FILE, 'r') as file:
    while True:
        line = file.readline()
        if not line: # End of file
            break
        dial, zero_count = rotate_dial(line.strip(), dial, zero_count)

print(zero_count)