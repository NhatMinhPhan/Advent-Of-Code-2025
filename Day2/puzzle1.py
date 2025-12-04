READ_FILE = 'example.txt'
invalid_sum = 0

def get_ID_range(range: str) -> tuple[int, int]:
    range_list: list[str] = range.split('-')
    start: int = int(range_list[0])
    end: int = int(range_list[-1])
    return start, end

def is_invalid_id(id: int) -> bool:
    id_str = str(id)
    if len(id_str) % 2 == 1:
        # Invalid IDs are made only of some sequence of digits repeated twice
        return False
    i = 0
    j = len(id_str) // 2
    while j < len(id_str):
        if id_str[i] != id_str[j]: # Not made of a sequence repeated twice
            return False
        i += 1
        j += 1
    return True
    

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