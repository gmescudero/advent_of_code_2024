from pprint import pprint

map = None
with open( "/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241206/data.txt") as f:
    # map = f.readlines()
    map = [ list(line.strip()) for line in f]

guard_pos = None
for x_idx,row in enumerate(map):
    try:
        y_idx = row.index('^')
        guard_pos = [x_idx, y_idx]
        map[x_idx][y_idx] = 'X'
    except ValueError:
        pass

map_height, map_width = len(map),len(map[0])

print(guard_pos)
pprint(map)
print((map_height, map_width))

UP    = (-1, 0)
DOWN  = ( 1, 0)
LEFT  = ( 0,-1)
RIGHT = ( 0, 1)
char_dir = {
    UP:'^',
    DOWN: 'v',
    LEFT: '<',
    RIGHT: '>'
}

count = 0
facing = UP

while True:

    new_pos = [x + y for x, y in zip(guard_pos, facing)]
    if new_pos[0] >= map_height or new_pos[0] < 0: break
    if new_pos[1] >= map_width  or new_pos[1] < 0: break

    if map[new_pos[0]][new_pos[1]] == '#':
        facing = (facing[1],-facing[0])
        # print(facing)

        # exit()
    else:
        map[guard_pos[0]][guard_pos[1]] =   'X'
        map[new_pos[0]][new_pos[1]] = char_dir[facing]
        guard_pos = new_pos
        count += 1
pprint(map)
print("")


# print(count)
count = 1
for row in map:
    count += row.count('X')


print(count)
