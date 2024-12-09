import pandas as pd
import copy

def isSafe(data:list, ascending:bool = None, idx:int = 0) -> bool:

    if len(data)-idx <= 1:
        return True
    l = data[idx]

    if abs(l-data[idx+1]) > 3 or l == data[idx+1]:
        return False

    if   l > data[idx+1]:
        if ascending == True:
            return False
        else:
            ascending = False
    elif l < data[idx+1]:
        if ascending == False:
            return False
        else:
            ascending = True
    return isSafe(data,ascending,idx=idx+1)

# df = pd.read_csv("https://adventofcode.com/2024/day/1/input")
# df = pd.read_csv("/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241202/data1.csv",header=None)

lines = []
with open("/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241202/data2.csv") as dataFile:
    lines = dataFile.readlines()

safeCount = len(lines)
for index, row in enumerate(lines):
    data = [int(val) for val in row.replace('\n','').split(', ')]
    # print(data)
    if not isSafe(data):
        safeCount -= 1

print(safeCount)


lines = []
with open("/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241202/data1.csv") as dataFile:
    lines = dataFile.readlines()

safeCount = len(lines)
for index, row in enumerate(lines):
    data = [int(val) for val in row.replace('\n','').split(', ')]
    # print(data)
    if not isSafe(data):
        damped = False
        for newIndex in range(len(data)):
           newData = copy.deepcopy(data)
           newData.pop(newIndex) 
           if isSafe(newData):
               damped = True
               break
        safeCount = safeCount-1 if not damped else safeCount

print(safeCount)