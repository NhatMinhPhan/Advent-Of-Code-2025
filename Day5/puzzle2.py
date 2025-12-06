READ_FILE = 'example.txt'
id_ranges: list[tuple[int, int]] = []
merged_ranges: list[tuple[int, int]] = []
fresh_total: int = 0

# File input
with open(READ_FILE, 'r') as file:
    while True:
        line = file.readline()
        if not line or line.strip() == '': # End of input
            break
        line = line.strip()
        split = line.split('-')
        start = int(split[0])
        end = int(split[1])
        id_ranges.append((start, end))

# Merge overlapping ranges
id_ranges.sort()
merged_ranges = [id_ranges[0]]
for current_start, current_end in id_ranges[1:]:
    last_merged_start, last_merged_end = merged_ranges[-1]

    # Check for overlap
    if current_start <= last_merged_end:
        # Merge by updating the end of the last merged range
        merged_ranges[-1] = (last_merged_start, max(last_merged_end, current_end))
    else:
        # No overlap, add the current range as a new range
        merged_ranges.append((current_start, current_end))

for id_range in merged_ranges:
    fresh_total += id_range[1] - id_range[0] + 1

print(fresh_total)