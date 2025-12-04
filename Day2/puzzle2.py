READ_FILE = 'example.txt'
invalid_sum = 0

def get_ID_range(range: str) -> tuple[int, int]:
    range_list: list[str] = range.split('-')
    start: int = int(range_list[0])
    end: int = int(range_list[-1])
    return start, end

def is_invalid_id(id: int) -> bool:
    id_str = str(id)
    is_invalid: bool = True
    # Invalid IDs made of some sequence of digits repeated n times must be divisible by n.
    for repeat_times in range(2, len(id_str) + 1, 1):
        is_invalid = True
        if len(id_str) % repeat_times != 0:
            continue
        indices: list[int] = []
        for i in range(repeat_times):
            indices.append(len(id_str) / repeat_times * i)
        while indices[-1] < len(id_str):
            # Check all indices
            for i in range(len(indices) - 1):
                # Check if char at each index in indices are the same.
                # If not, try a different repeat_times in the next iteration of the outermost loop.
                first_index = int(indices[i])
                second_index = int(indices[i+1])
                if id_str[first_index] != id_str[second_index]: # Not made of a sequence repeated twice
                    is_invalid = False
                    break
            if not is_invalid:
                break
            for i in range(len(indices)):
                indices[i] += 1
        if is_invalid: # after the while loop, meaning the sequence repeats in this iteration
            return True
    return False
    

with open(READ_FILE, 'r') as file:
    content : str = file.read().strip()
    ranges = content.split(',')
    for r in ranges:
        invalid_ids: list[int] = []
        start, end = get_ID_range(r)
        for id in range(start, end + 1, 1):
            if is_invalid_id(id):
                invalid_ids.append(id)
        invalid_sum += sum(invalid_ids)
print(invalid_sum)