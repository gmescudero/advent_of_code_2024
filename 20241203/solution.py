import re

matches = None
with open("/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241203/data.txt") as file:
    # matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)",file.read())
    matches = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)",file.read())

print(matches)
val = 0.0
do = True
for m in matches:
    if   m == "do()":
        do = True
    elif m == "don't()":
        do = False
    elif do:
        numbers = m.replace('mul(','').replace(')','').split(',')
        print(numbers)
        val += int(numbers[0])*int(numbers[1])

print(val)

