
import re
text = []
with open( "/home/gmoreno/Workspace/pruebas/adventOfCode2024/20241204/data.txt") as f:
    text = f.readlines()

# MATCH = r"XMAS|SAMX"
MATCH1 = r"XMAS"
MATCH2 = r"SAMX"
rows = len(text)
cols = len(text[0])-1

count = 0


print(f"DATA rows:{rows} cols:{cols}")
print("--------------------------------")
# Horizontals
for diag in text:
    matches = re.findall(MATCH1, diag) + re.findall(MATCH2, diag)
    count += len(matches)
    print(f"{len(matches)} {diag.strip()}")
    
print("--------------------------------")


# Verticals
for c in range(cols):
    diag = ''.join([text[r][c] for r in range(rows)])
    matches = re.findall(MATCH1, diag) + re.findall(MATCH2, diag)
    count += len(matches)
    print(f"{len(matches)} {diag}")
print("--------------------------------")


# Diagonal 1 (\)
for i in range(rows-3):
    # Diagonal downwards
    diag = ''.join([text[r+i][r] for r in range(rows-i)])
    matches = re.findall(MATCH1, diag) + re.findall(MATCH2, diag)
    count += len(matches)
    print(f"{len(matches)} {diag}")
print("--------------------------------")
for i in range(1,cols-3):
    # Diagonal upwards
    diag = ''.join([text[r][r+i] for r in range(rows-i)])
    matches = re.findall(MATCH1, diag) + re.findall(MATCH2, diag)
    count += len(matches)
    print(f"{len(matches)} {diag}")
print("--------------------------------")


# Diagonal 2 (/)
for i in range(rows-3):
    # Anti Diagonal upwards
    diag = ''.join([text[-(r+1+i)][r] for r in range(rows-i)])
    matches = re.findall(MATCH1, diag) + re.findall(MATCH2, diag)
    count += len(matches)
    print(f"{len(matches)} {diag}")
print("--------------------------------")

for i in range(1,cols-3):
    # Anti Diagonal downwards
    diag = ''.join([text[-(r+1)][r+i] for r in range(rows-i)])
    matches = re.findall(MATCH1, diag) + re.findall(MATCH2, diag)
    count += len(matches)
    print(f"{len(matches)} {diag}")
print("--------------------------------")

print(count)
