from pprint import pprint
import copy as cp
from dataclasses import dataclass 


UP    = (-1, 0)
DOWN  = ( 1, 0)
LEFT  = ( 0,-1)
RIGHT = ( 0, 1)
CHAR_DIR = {
    UP:'^',
    DOWN: 'v',
    LEFT: '<',
    RIGHT: '>'
}

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

# nodes = []

# for x,row in enumerate(map):
#     for y,elem in enumerate(row):
#         if elem == '#': nodes.append((x,y))

# print(nodes)


# dict_connections = {}
# for i,nd in enumerate(nodes):
#     x,y = nd
#     connections = []
#     for j,hit_nd in enumerate(nodes):
#         if nd != hit_nd:
#             hit_x,hit_y = hit_nd
#             if x+1 == hit_x and y < hit_y: connections.append((hit_x,hit_y))
#             if x-1 == hit_x and y > hit_y: connections.append((hit_x,hit_y))
#             if y+1 == hit_y and x < hit_x: connections.append((hit_x,hit_y))
#             if y-1 == hit_y and x > hit_x: connections.append((hit_x,hit_y))

#     dict_connections.update({nd:connections})
# pprint(dict_connections)




def step_pos(pos,facing):
    return [x + y for x, y in zip(pos, facing)]

def de_step_pos(pos,facing):
    return [x - y for x, y in zip(pos, facing)]

def rotate_pos(facing):
    return (facing[1],-facing[0])


# first_hit = None
# for i in range(guard_pos[0],-1, -1):
#     if (i,guard_pos[1]) in nodes:
#         first_hit = (i,guard_pos[1])

# print(f"first hit: {first_hit}")



@dataclass
class Hit:
    pos:list
    facing:list


start_pos = cp.copy(guard_pos)
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
        map[new_pos[0]][new_pos[1]] = CHAR_DIR[facing]
        guard_pos = new_pos

for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col] == 'X':
            facing = UP
            guard_pos = cp.copy(start_pos)
            new_map = cp.deepcopy(map)
            new_map[row][col] = '#'
            hits = []
            last_hit = Hit(guard_pos,facing)
            while True:
                new_pos = step_pos(guard_pos,facing)
                if new_pos[0] >= map_height or new_pos[0] < 0: break
                if new_pos[1] >= map_width  or new_pos[1] < 0: break

                if new_map[new_pos[0]][new_pos[1]] == '#':
                    last_hit = Hit(guard_pos, facing)
                    if last_hit in hits: 
                        count +=1
                        break # Found loop
                    hits.append(last_hit)
                    facing = rotate_pos(facing)
                    # print(facing)

                    # exit()
                else:
                    new_map[guard_pos[0]][guard_pos[1]] =   'X'
                    new_map[new_pos[0]][new_pos[1]] = CHAR_DIR[facing]
                    guard_pos = new_pos
            # pprint(new_map)


print(count)