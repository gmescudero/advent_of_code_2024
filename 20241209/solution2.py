from pprint import pprint

text = None
with open("/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241209/data.txt") as f:
    text = f.read()

# Get raw file data
block_empty = [int(c) for c in text]
print(block_empty)

# Get the data extended 
extended_data = []
just_data = []
data_blocks_num = 0
for i,sz in enumerate(block_empty):
    if i % 2 == 0:
        extended_data += [int(i/2) for _ in range(sz)]
        just_data += [int(i/2) for _ in range(sz)]
        data_blocks_num += 1
    else:
        extended_data += ['.' for _ in range(sz)]

print(extended_data)

def find_free_space(data:list, size:int,  start_index:int=0, stop_index:int = None) -> tuple:

    if stop_index is None: stop_index = len(data)

    free_size = 0
    for i in range(start_index, stop_index):
        if data[i] == '.':
            free_size += 1
        elif data[i] != '.' and free_size != 0 and free_size >= size:
            return (i-free_size,free_size)
        else:
            free_size = 0
    return None,None

        
blocks_idx = len(extended_data)-1
while blocks_idx > extended_data.index('.'):
    block_size = 0
    block_id = extended_data[blocks_idx]
    if block_id != '.': 
        while extended_data[blocks_idx-block_size] == block_id and block_size < len(extended_data):
            block_size += 1
        
        free_idx,free_size = find_free_space(extended_data, block_size, extended_data.index('.'),blocks_idx)
        if free_idx is not None:
            for i in range(block_size):
                extended_data[free_idx+i] = extended_data[blocks_idx-i]
                extended_data[blocks_idx-i] = '.'
        # print("".join([str(c) for c in extended_data]))
        blocks_idx -= block_size
    else:
        blocks_idx -= 1
    print(f"block idx {blocks_idx}, first empty {extended_data.index('.')}")


print(extended_data)
print("".join([str(c) for c in extended_data]))

for i in range(len(extended_data)):
    if extended_data[i] == '.': extended_data[i] = 0

checksum = sum([i*c for i,c in enumerate(extended_data)])
print(checksum)
