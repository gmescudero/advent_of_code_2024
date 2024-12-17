from pprint import pprint
import copy as cp
from dataclasses import dataclass
import numpy as np

def print_map(map, cell_width:int = 3, return_text:bool=False):
    full_map_text = ""
    for i,row in enumerate(map):
        text = f"{i:3}:\t"
        for elem in row:
            str_elem = str(elem)
            text += "".join([' ' for _ in range(cell_width-len(str_elem))]) + str_elem + ','
        full_map_text += text+"\n"
    if return_text:
        return full_map_text
    else:
        print(full_map_text)


start = None
end = None
map = []
with open("C:\\Users\\Ad Maiorem\\Desktop\\Develop\\Workspace\\python\\advent_of_code_2024\\20241216\\data.txt") as f:
    for ln in f.readlines():
        map.append(list([c for c in ln.strip()]))
        for y,elem in enumerate(map[-1]):
            if elem == 'E':
                end = (len(map)-1,y)
            if elem == 'S':
                start = (len(map)-1,y)



map_height = len(map)
map_width = len(map[0])

# pprint(map)
# print(start)
# print(end)

NORTH = (-1,0)
SOUTH = (1,0)
WEST = (0,-1)
EAST = (0,1)

@dataclass
class Pose:
    x:int
    y:int
    facing:tuple

    def __hash__(self):
        return hash(f"{self.x},{self.y}")

    def check_available(self):
        x,y = (self.x, self.y)
        if x < 0 or x >= map_height or y < 0 or y >= map_width or map[x][y] == '#':
            return False
        else:
            return True
        
    def step_forward(self):
        new_pose = Pose(self.x+self.facing[0], self.y+self.facing[1], self.facing)
        if new_pose.check_available():
            return new_pose
        return None
    
    def step_right(self):
        new_facing = (self.facing[1],-self.facing[0])
        new_pose = Pose(self.x+new_facing[0],self.y+new_facing[1], new_facing)
        if new_pose.check_available():
            return new_pose
        return None
        

    def step_left(self):
        new_facing = (-self.facing[1],self.facing[0])
        new_pose = Pose(self.x+new_facing[0],self.y+new_facing[1], new_facing)
        if new_pose.check_available():
            return new_pose
        return None
    
    def get_availables(self):
        available_poses = []
        forward = self.step_forward()
        right = self.step_right()
        left = self.step_left()
        

        if None != forward: available_poses.append((forward,1))
        if None != right: available_poses.append((right,1001))
        if None != left: available_poses.append((left,1001))

        return available_poses

class PrioQueue:
    elements:dict = {}

    def __init__(self, starting_element=None, starting_prio:int=0):
        self.elements = dict({})
        if starting_element is not None:
            self.add_element(starting_element, starting_prio)
    
    def __repr__(self):
        text = "Priority Queue:\n"
        for key,val in self.elements.items():
            text += f"\t{key}:{val}\n"
        return text

    def add_element(self,element,prio):
        if prio not in self.elements.keys():
            self.elements.update({prio:[element]})
        else:
            vals = self.elements[prio]
            self.elements.update({prio:vals+[element]})
    
    def get_element(self):
        key = min(self.elements.keys())
        if len(self.elements[key]) == 1:
            val = self.elements.pop(key)[0]
        else:
            val = self.elements[key].pop()
        return key,val
    
    def get_size(self):
        return len(self.elements.keys())

pose = Pose(end[0],end[1],WEST)
queue = PrioQueue(pose,0)

print_map(map)
while queue.get_size() > 0:
    # print(queue)
    current_score,current_pose = queue.get_element()
    print(f"Score: {current_score}, {current_pose}")
    if map[current_pose.x][current_pose.y] == 'S': 
        print(queue)
        print(f"\t => Obtained score {current_score}")
        break
    map_score = map[current_pose.x][current_pose.y] if type(map[current_pose.x][current_pose.y]) != str else 1e300
    if map_score > current_score:
        map[current_pose.x][current_pose.y] = current_score
        # print_map(map,5)
        available_steps = current_pose.get_availables()
        for pose, score in available_steps:
            queue.add_element(pose,score+current_score)


with open("result_map.txt","+w") as f:
    f.write(print_map(map,6,True))


# 85440 is too high
# 85432 is the right answer