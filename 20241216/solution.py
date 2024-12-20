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
    facing:tuple = NORTH
    prev:any = None

    def __hash__(self):
        return hash(f"{self.x},{self.y}")

    def __repr__(self):
        chars = {
            NORTH:"NORTH",
            SOUTH:"SOUTH",
            WEST:"WEST",
            EAST:"EAST",
        }
        return f"Pose(x:{self.x},y:{self.y},facing:{chars[self.facing]})"

    def __eq__(self, value):
        if type(value) != Pose: return False
        return True if self.x == value.x and self.y == value.y else False

    def check_available(self):
        x,y = (self.x, self.y)
        if x < 0 or x >= map_height or y < 0 or y >= map_width or map[x][y] == '#':
            return False
        else:
            return True
        
    def step_forward(self):
        new_pose = Pose(self.x+self.facing[0], self.y+self.facing[1], self.facing, prev = self)
        if new_pose.check_available():
            return new_pose
        return None
    
    def step_right(self):
        new_facing = (self.facing[1],-self.facing[0])
        new_pose = Pose(self.x+new_facing[0],self.y+new_facing[1], new_facing, prev = self)
        if new_pose.check_available():
            return new_pose
        return None
        

    def step_left(self):
        new_facing = (-self.facing[1],self.facing[0])
        new_pose = Pose(self.x+new_facing[0],self.y+new_facing[1], new_facing, prev = self)
        if new_pose.check_available():
            return new_pose
        return None
    
    def turn_back(self):
        self.facing = (-self.facing[0],-self.facing[1])


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
    invert:bool = False

    def __init__(self, starting_element=None, starting_prio:int=0, invert:bool = False):
        self.elements = dict({})
        self.invert = invert
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
        key = 0
        if self.invert == False:
            key = min(self.elements.keys())
        else:
            key = max(self.elements.keys())
        if len(self.elements[key]) == 1:
            val = self.elements.pop(key)[0]
        else:
            val = self.elements[key].pop()
        return key,val
    
    def get_size(self):
        return len(self.elements.keys())

def dijkstra(start_pos, end_pos, start_prio = 0):
    visited = set({})
    queue = PrioQueue(start_pos,start_prio)
    while queue.get_size() > 0:
        current_score,current_pose = queue.get_element()
        visited.add(current_pose)
        # print(f"Score: {current_score}, {current_pose}")
        if current_pose == end_pos: 
            return current_pose, current_score
        available_steps = current_pose.get_availables()
        for pose, score in available_steps:
            if pose not in visited:
                queue.add_element(pose,score+current_score)
    return None,None


end_pose = Pose(end[0],end[1])
start_pose = Pose(start[0], start[1])

print("Part 1")
# print_map(map)
# pose = Pose(start[0],start[1],EAST)
# pose,score = dijkstra(pose,end_pose)
pose = Pose(end[0],end[1],WEST)
pose,score = dijkstra(pose,start_pose)
print(f"Reached {pose} with score = {score}")


# Part1:
# 85440 is too high
# 85432 is the right answer
# Part2: TODO

print("Part 2")
print("Compute Path")
def compute_path(reached_pose:Pose) -> list:
    path = []
    while reached_pose != None:
        path.append(reached_pose)
        reached_pose = reached_pose.prev
    return path

path = compute_path(pose)
dist = len(path)
# pprint(path)
print(f"Distance = {dist}")

places = set({})
for elem in path:
    places.add(elem)
path.reverse()
for i,p in enumerate(path):
    choices = p.get_availables()
    if len(choices) > 1:
        sols = []
        for ch,st_sc in choices:
            sol = dijkstra(ch,start_pose,st_sc)
            if sol[0] is not None:
                sols.append(sol)
        if len(sols) > 0:
            min_score = min([c[1] for c in sols])
            for sol in sols:
                if sol[1] == min_score:
                    for place in compute_path(sol[0]):
                        places.add(place)

print(len(places))
    
for pl in places:
    map[pl.x][pl.y] = 'O'


# 480 is too high
# 465 is the answer



with open("result_map.txt","+w") as f:
    f.write(print_map(map,2,True))