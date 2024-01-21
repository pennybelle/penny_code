data = ['1', '3', '5']

# attempt 1
def convert_add_old(data):
    added = []
    for item in data:
        added.append(int(item))
    return sum(added)

# attempt 2
def convert_add(data): return sum(map(int, data))

print(convert_add(data))
    
data = ['apple', 'orange', 'apple', 'banana', 'apple', 'orange']

def duplicate_names(data):
    copy, dupes = [], []
    for item in data:
        if item not in copy:
            copy.append(item)
        elif item not in dupes:
            dupes.append(item)
    if dupes:
        return ', '.join(dupes)
    else:
        return 'No duplicates'

print(duplicate_names(data))