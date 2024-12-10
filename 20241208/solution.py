from dataclasses import dataclass
from pprint import pprint
import numpy as np
import copy as cp

map = []

with open( "/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241208/data.txt") as f:
    # text = f.readlines()
    for line in f:
        map.append(list(line.strip()))
map_height, map_width = len(map),len(map[0])

pprint(map)

@dataclass 
class Node:
    x:int
    y:int

    def add(self, v):
        return Vector(self.x+v.x, self.y+v.y)

    def __hash__(self):
        return self.x*map_width + self.y

@dataclass 
class Antenna(Node):
    freq:str

class Vector(Node):
    def __post_init__(self):
        self.dist = np.sqrt(self.x**2 + self.y**2)
    


antennas = []
for i,row in enumerate(map):
    for j,elem in enumerate(row):
        if elem != '.': antennas.append(Antenna(i,j,elem))

print(antennas)

count = 0
antinodes = set({})
for anten in antennas:
    for reson in antennas:
        if anten != reson and anten.freq == reson.freq: 
            dir = Vector(reson.x-anten.x, reson.y-anten.y)
            vect = cp.copy(dir)
            antinode = anten.add(vect)
            antinode = anten.add(vect)
            while antinode.x < map_height and antinode.y < map_width and antinode.x >= 0 and antinode.y >= 0:
                antinodes.add(antinode)
                vect = vect.add(dir)
                antinode = anten.add(vect)

            # vect = dir.add(dir)
            # antinode = anten.add(vect)
            # if antinode.x < map_height and antinode.y < map_width and antinode.x >= 0 and antinode.y >= 0:
            #     antinodes.add(antinode)
            #     # map[antinode.x][antinode.y] = "#" if map[antinode.x][antinode.y] == '.' else map[antinode.x][antinode.y]
            #     if map[antinode.x][antinode.y] != "#":
            #         map[antinode.x][antinode.y] = "#"
            #         count += 1

for antinode in antinodes:
    if map[antinode.x][antinode.y] == ".":
        map[antinode.x][antinode.y] = "#"

pprint(map)
pprint(antinodes)
print(len(antinodes))
with open("/home/gmoreno/Workspace/pruebas/map.txt","+w") as f:
    for row in map:
        f.write(''.join(row)+"\n")