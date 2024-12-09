import pandas as pd


# df = pd.read_csv("https://adventofcode.com/2024/day/1/input")
df = pd.read_csv("/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241201/20241201-1.csv",header=None)

firstList = []
secondList = []

for index, row in df.iterrows():
    print(f"index: {index}, row0: {row.iloc[0]}, row1: {row.iloc[1]}")
    firstList.append(row.iloc[0])
    secondList.append(row.iloc[1])



firstList.sort()
secondList.sort()
val = 0.0
for l1, l2 in zip(firstList,secondList):
    val = val+ abs(l1-l2)

print(f"sum of minimums:{val}")
df = pd.read_csv("/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241201/20241201-2.csv",header=None)

firstList = []
secondList = []

for index, row in df.iterrows():
    print(f"index: {index}, row0: {row.iloc[0]}, row1: {row.iloc[1]}")
    firstList.append(row.iloc[0])
    secondList.append(row.iloc[1])

val = 0.0
for l1 in firstList:
    for l2 in secondList:
        if l1 == l2:
            val += l1
            
print(f"similarity score:{val}")