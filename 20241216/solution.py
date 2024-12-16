from pprint import pprint
import copy as cp
from dataclasses import dataclass
import numpy as np

def print_map(map, cell_width:int = 3):
    for i,row in enumerate(map):
        text = f"{i}:\t"
        for elem in row:
            str_elem = str(elem)
            text += "".join([' ' for _ in range(cell_width-len(str_elem))]) + str_elem + ','
        print(text)


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

pprint(map)
print(start)
print(end)


def check_available(pos:tuple) -> bool:
    x,y = pos
    return True if x < map_height and x >= 0 and y < map_width and y >= 0 and map[x][y] != '#' else False

def step_forward(pos:tuple,facing:tuple) -> tuple:
    return (pos[0]+facing[0], pos[1]+facing[1])

def rotate(facing:tuple, clockwise:bool = True) -> tuple:
    return (facing[1],-facing[0]) if clockwise else (-facing[1],facing[0])


NORTH = (-1,0)
SOUTH = (1,0)
WEST = (0,-1)
EAST = (0,1)

for i,row in enumerate(map):
    for j, elem in enumerate(row):
        if elem == '.':
            map[i][j] = int(np.ceil(np.sqrt((end[0]-i)**2 + (end[1]-j)**2)))


print_map(map)


@dataclass
class Pose:
    x:int
    y:int
    facing:tuple

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
        if None != left and None != right:
            if map[left.x][left.y] > map[right.x][right.y]:
                aux = available_poses.pop()
                available_poses.insert(-2,aux)

        return available_poses

nodes = []
connections = {}

def find_path(pose:Pose, score:int = 0, path=[]):
    print(f"Score: {score}, Pose: {pose}")
    path.append(pose)
    if map[pose.x][pose.y] == 'E': return score
    if pose in nodes: return -1
    poses_w_score = pose.get_availables()
    if len(poses_w_score) >= 2:
        nodes.append(pose)
    elif len(poses_w_score) == 0 :return -1
    for ps,sc in poses_w_score:
        if ps not in path:
            new_score = find_path(ps,score+sc)
            if new_score != -1: 
                return new_score
        else: 
            new_score = -1
    return -1
    

pose = Pose(start[0],start[1],EAST)
print(find_path(pose))
print_map(map)
pprint(nodes)

queue = [(pose,0)]
def queue_step(queue:list):
    current_pose,score = queue.pop(0)
    print(f"Score: {score}, Pose: {current_pose}")
    if map[current_pose.x][current_pose.y] == 'E': return score
    available_steps = current_pose.get_availables()
    if len(available_steps) == 0:
        return queue_step(queue)
    elif len(queue) == 0:
        queue = list([(pose,sc+score) for pose,sc in available_steps])
    else:
        for pose,sc in available_steps:
            for i,queue_elem in enumerate(queue):
                if sc+score < queue_elem[1]:
                    queue.insert(i,(pose,sc+score))
                    break
    return queue_step(queue)

print_map(map)
print(queue_step(queue))
