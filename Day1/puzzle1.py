READ_FILE = 'example.txt'
dial: int = 50
zero_count = 0

def rotate_dial(line: str, dial: int) -> int:
    amount: int = int(line[1:])
    match line[0]:
        case 'L':
            dial -= amount
            pass
        case 'R':
            dial += amount
            pass
    return dial

# File input
with open(READ_FILE, 'r') as file:
    while True:
        line = file.readline()
        if not line: # End of file
            break
        dial = rotate_dial(line.strip(), dial)
        # Since the circular dial can point 0-99, 100 is equivalent to 0.
        # 200 is equivalent to 0, and so is 300, 400, ... , -100, -200, etc.
        # Because of this, check for dial % 100.
        if dial % 100 == 0:
            zero_count += 1

print(zero_count)