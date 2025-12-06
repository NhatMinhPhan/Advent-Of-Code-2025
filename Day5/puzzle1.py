READ_FILE = 'example.txt'
id_ranges: list[tuple[int, int]] = []
num_of_fresh_ids: int = 0

def is_fresh(current_id: int) -> bool:
    for id_range in id_ranges:
        if (id_range[0] <= current_id <= id_range[1]):
            return True
    return False

# File input
append_ranges: bool = True
with open(READ_FILE, 'r') as file:
    while True:
        line = file.readline()
        if not line: # End of file
            break
        line = line.strip()

        if line == '' and append_ranges:
            append_ranges = False
            continue

        if append_ranges:
            split = line.split('-')
            start = int(split[0])
            end = int(split[1])
            id_ranges.append((start, end))
            continue
        
        current_id = int(line)
        num_of_fresh_ids = num_of_fresh_ids + 1 if is_fresh(current_id) else num_of_fresh_ids

print(num_of_fresh_ids)