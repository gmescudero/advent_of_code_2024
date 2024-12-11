
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

# Compress the data
for i in range(len(extended_data)-1, 0, -1):
    empty_idx = extended_data.index('.')
    if i < empty_idx: 
        break
    elif extended_data[i] != '.':
        extended_data[extended_data.index('.')] = extended_data[i]
        extended_data[i] = '.'

while extended_data[-1] == '.': extended_data.pop()

print(extended_data)
print("".join([str(c) for c in extended_data]))
# 0099811188827773336446555566
# 0099811188827773336446555566

checksum = sum([i*c for i,c in enumerate(extended_data)])
print(checksum)
