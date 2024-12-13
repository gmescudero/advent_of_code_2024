from pprint import pprint
import copy as cp

text = None
with open("/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241210/data.txt") as f:
    text = f.readlines()


hiking_map = []
for l in text:
    hiking_row = []
    for e in l.strip():
        hiking_row.append(int(e) if e != '.' else '.')
    hiking_map.append(hiking_row)
    # hiking_map.append([int(c) for c in l.strip()])

hiking_map_height = len(hiking_map)
hiking_map_width  = len(hiking_map[0])
# pprint(hiking_map)

def seek_paths(hmap:list, pos:list) -> int:
    x,y = pos
    # print(f"Steping {(x,y)} with value {hmap[x][y]}")

    if hmap[x][y] == 9: 
        # print("\tAdd score")
        # hmap[x][y] = '.' # Uncomment this for solution for first problem
        return 1

    score = 0
    steps = ((x+1,y),(x,y+1),(x-1,y),(x,y-1))
    for new_x, new_y in steps:
        if  new_x >= 0 and new_x < hiking_map_height \
                and new_y >= 0 and new_y < hiking_map_width \
                and hmap[new_x][new_y] == hmap[x][y]+1:

            score += seek_paths(hmap, (new_x,new_y))
    return score
        

score_sum = 0
for i,row in enumerate(hiking_map):
    for j,element in enumerate(row):
        if element == 0:
            score_sum += seek_paths(cp.deepcopy(hiking_map), (i,j))

print(score_sum)