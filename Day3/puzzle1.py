READ_FILE = 'example.txt'
total_joltage = 0

def get_bank_joltage(bank: str) -> int:
    assert len(bank) >= 2, "len(bank) must be at least 2"
    # Get the 2 greatest digits
    # The greatest digit which acts as the 1st digit must be within [:-1]
    # If the greatest digit is at index -1,  it can only act as the 2nd digit.
    # Otherwise, the 2nd digit is the 2nd-greatest digit found to the right of 
    # Put them together
    first, second = 0, 0
    batteries = [int(battery) for battery in bank]

    greatest = batteries.index(max(batteries))
    temp_greatest = batteries[greatest]
    if greatest == len(bank) - 1:
        batteries[greatest] = -1 # Make the program ignore the index of the battery with the greatest joltage
    else:
        for i in range(0, greatest + 1):
            batteries[i] = -1 # Only find the second-greatest digit after greatest
    second_greatest = batteries.index(max(batteries))
    batteries[greatest] = temp_greatest
    
    if greatest == len(bank) - 1:
        second = batteries[greatest]
        first = batteries[second_greatest]
    else:
        first = batteries[greatest]
        second = batteries[second_greatest]
    return int(f'{first}{second}')


# File input
with open(READ_FILE, 'r') as file:
    while True:
        line = file.readline()
        if not line: # End of file
            break
        total_joltage += get_bank_joltage(line.strip())
        print(get_bank_joltage(line.strip()))
print(total_joltage)