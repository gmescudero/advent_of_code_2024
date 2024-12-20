from pprint import pprint
import copy as cp
from dataclasses import dataclass
import os
import re
from numpy import round

file_path = os.path.dirname(os.path.abspath(__file__))

def print_map(map, cell_width:int = 3, return_text:bool=False, shrink:bool=False):
    full_map_text = ""
    for i,row in enumerate(map):
        text = f"{i:3}:\t"
        for elem in row:
            str_elem = str(elem)
            if shrink:
                text += str_elem
            else:
                text += "".join([' ' for _ in range(cell_width-len(str_elem))]) + str_elem + ','
        full_map_text += text+"\n"
    if return_text:
        return full_map_text
    else:
        print(full_map_text)


SECONDS = 100
MAP_SIZE = (101,103)
# MAP_SIZE = (11,7)

@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int
    total_seconds: int = 0

    def move(self, seconds:int = 1):
        self.total_seconds += seconds
        self.x += self.vx*seconds
        self.x %= MAP_SIZE[0]
        if self.x < 0:
            self.x += MAP_SIZE[0]

        self.y += self.vy*seconds
        self.y %= MAP_SIZE[1]
        if self.y < 0:
            self.y += MAP_SIZE[1]


text = None
robots = []
with open(file_path +"/data.txt") as f:
    for line in f:
        text = line.strip()
        pos,vel = line.split(" ")
        pos = pos.replace("p=","")
        vel = vel.replace("v=","")
        x,y = pos.split(",")
        vx,vy = vel.split(",")
        x,y = int(x),int(y)
        vx,vy = int(vx),int(vy)
        robot = Robot(x,y,vx,vy)
        robots.append(robot)
part_two_robots = cp.deepcopy(robots)
    
pprint(robots)


for robot in robots:
    robot.move(SECONDS)

cuadrants = [0,0,0,0]
mapa = [[0 for _ in range(MAP_SIZE[0])] for _ in range(MAP_SIZE[1])]
for robot in robots:
    if   robot.x < MAP_SIZE[0]//2 and robot.y < MAP_SIZE[1]//2:
        cuadrants[0] += 1
    elif robot.x > MAP_SIZE[0]//2 and robot.y < MAP_SIZE[1]//2:
        cuadrants[1] += 1
    elif robot.x < MAP_SIZE[0]//2 and robot.y > MAP_SIZE[1]//2:
        cuadrants[2] += 1
    elif robot.x > MAP_SIZE[0]//2 and robot.y > MAP_SIZE[1]//2:
        cuadrants[3] += 1
    mapa[robot.y][robot.x] += 1
    

print_map(mapa,2)
pprint(cuadrants)
print(cuadrants[0]*cuadrants[1]*cuadrants[2]*cuadrants[3])


# Part two
fd = open(file_path + "/part_two.txt","w+")
fd.close()

# Pattern starting at 72 seconds
for robot in part_two_robots:
    robot.move(72)

# Pattern repeating every 103 seconds
for i in range(7000):
    mapa = [[' ' for _ in range(MAP_SIZE[0])] for _ in range(MAP_SIZE[1])]
    for robot in part_two_robots:
        robot.move(103)
        if type(mapa[robot.y][robot.x]) == int:
            mapa[robot.y][robot.x] += 1
        else:
            mapa[robot.y][robot.x] = 1
    with open(file_path + "/part_two.txt","a") as f:
        f.write(f"Second:{part_two_robots[0].total_seconds}\n")
        f.write(print_map(mapa,2,True,True))
        f.write("\n\n\n")
    if i%1000 == 0: print(f"Iterating over {i} out of 7000")

# Search for 11111111111111111111111111111 in the file to find the answer
# 71 is not correct
# 10519 is not correct
# 6354 is too low 
# the answer is 6355