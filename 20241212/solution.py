from pprint import pprint
import copy as cp
from dataclasses import dataclass
import os
file_path = os.path.dirname(os.path.abspath(__file__))

map = []
with open(file_path +"/data.txt") as f:
    for ln in f.readlines():
        map.append([c for c in ln.strip()])

map_height = len(map)
map_width = len(map[0])
# pprint(map)

NORTH = (-1, 0)
SOUTH = ( 1, 0)
EAST  = ( 0, 1)
WEST  = ( 0,-1)

@dataclass
class Pose:
    x:int
    y:int
    facing:tuple = None
    prev:any = None

    LEFT=0
    FRONT=1
    RIGHT=2
    BACK=3

    def __hash__(self):
        return hash(f"{self.x},{self.y}")

    def __repr__(self):
        chars = {
            NORTH:"NORTH",
            SOUTH:"SOUTH",
            WEST:"WEST",
            EAST:"EAST",
            None:"None"
        }
        return f"Pose(x:{self.x},y:{self.y},facing:{chars[self.facing]})"

    def __eq__(self, value):
        if type(value) != Pose: return False
        return True if self.x == value.x and self.y == value.y and self.facing == value.facing else False
    
    def check_available(self):
        x,y = (self.x, self.y)
        if x < 0 or x >= map_height or y < 0 or y >= map_width:
            return False
        else:
            return True
        
    def rotate_clockwise(self):
        new_facing = (self.facing[1],-self.facing[0])
        return Pose(self.x,self.y, new_facing)

    def rotate_anticlockwise(self):
        new_facing = (-self.facing[1],self.facing[0])
        return Pose(self.x,self.y, new_facing)

    def step_forward(self):
        if self.facing is None: return None
        new_pose = Pose(self.x+self.facing[0], self.y+self.facing[1], self.facing, prev = self)
        if new_pose.check_available():
            return new_pose
        return None
    
    def step_back(self):
        if self.facing is None: return None
        new_facing = (-self.facing[0],-self.facing[1])
        new_pose = Pose(self.x+new_facing[0],self.y+new_facing[1], new_facing, prev = self)
        if new_pose.check_available():
            return new_pose
        return None
    
    def step_right(self):
        if self.facing is None: return None
        new_facing = (self.facing[1],-self.facing[0])
        new_pose = Pose(self.x+new_facing[0],self.y+new_facing[1], new_facing, prev = self)
        if new_pose.check_available():
            return new_pose
        return None
    
    def step_left(self):
        if self.facing is None: return None
        new_facing = (-self.facing[1],self.facing[0])
        new_pose = Pose(self.x+new_facing[0],self.y+new_facing[1], new_facing, prev = self)
        if new_pose.check_available():
            return new_pose
        return None
    
    
    def get_availables(self, moni:str = None):
        available_poses = []
        forward = self.step_forward()
        right = self.step_right()
        left = self.step_left()
        back = self.step_back()
        
        if None != left: available_poses.append(left)
        if None != forward: available_poses.append(forward)
        if None != right: available_poses.append(right)
        if None != back: available_poses.append(back)

        poses_in_area = []
        if None == moni:
            poses_in_area = available_poses
        else:
            for elem in available_poses:
                if map[elem.x][elem.y] == moni:
                    poses_in_area.append(elem)

        return poses_in_area

def get_area(start:Pose):
    moni = map[start.x][start.y]

    area = 0
    perimeter = 0
    vertexes = 0
    visited = []
    to_visit = [start]
    
    while len(to_visit) > 0:
        pose = to_visit.pop(0)
        if pose not in visited: 
            area += 1
            visited.append(pose)
            new_poses = (Pose(pose.x+1,pose.y),Pose(pose.x-1,pose.y),Pose(pose.x,pose.y+1),Pose(pose.x,pose.y-1))
            for new_pose in new_poses:
                if new_pose.check_available():
                    if map[new_pose.x][new_pose.y] != moni:
                        perimeter += 1
                    else:
                        to_visit.append(new_pose)
                else:
                    perimeter += 1
            # Compute vertexes to get sides
            possible_vertexes = (
                (new_poses[0],new_poses[2]),
                (new_poses[2],new_poses[1]),
                (new_poses[1],new_poses[3]),
                (new_poses[3],new_poses[0]),
            )
            for v1,v2 in possible_vertexes:
                v1_is_moni = v1.check_available()
                if v1_is_moni:
                    if map[v1.x][v1.y] != moni:
                        v1_is_moni = False
                v2_is_moni = v2.check_available()
                if v2_is_moni:
                    if map[v2.x][v2.y] != moni:
                        v2_is_moni = False
                if not v2_is_moni and not v1_is_moni:
                    vertexes += 1
                elif v2_is_moni and v1_is_moni:
                    if map[v1.x][v2.y] != moni or map[v2.x][v1.y] != moni:
                        vertexes += 1
                

    return area,perimeter,vertexes,visited
        

visited = []
areas = {}

for i,row in enumerate(map):
    for j,_ in enumerate(row):
        start_pose = Pose(i,j)
        if start_pose not in visited:
            area,perimeter,vertexes,new_visited = get_area(start_pose)
            visited += new_visited
            areas.update({(start_pose,map[start_pose.x][start_pose.y]):(area,perimeter,vertexes)})


# start_pose = Pose(0,0,EAST)
# print(get_area(start_pose))

# pprint(areas)

price = 0
for area,perimeter,_ in areas.values():
    price += perimeter*area

print(price)

price = 0
for area,_,vertexes in areas.values():
    price += vertexes*area

print(price)
