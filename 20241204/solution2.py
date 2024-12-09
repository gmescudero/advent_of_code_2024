import re
text = []
with open( "/home/gmoreno/Workspace/pruebas/adventOfCode2024/20241204/data.txt") as f:
    text = f.readlines()

MATCH = r"MAS|SAM"


rows = len(text)
cols = len(text[0])-1

count = 0

for r in range(rows-2):
    for c in range(cols-2):
        x_piece1 = ''.join([text[r+i][c+i] for i in range(3)])
        x_piece2 = ''.join([text[r+2-i][c+i] for i in range(3)])
        if re.match(MATCH,x_piece1) is not None and re.match(MATCH,x_piece2) is not None: count += 1
        # print(re.match(MATCH,x_piece1))
        # print(x_piece1)
        # if (c == 1): exit()
        # print(x_piece1)
        print(f"p:{r},{c} x1: { x_piece1}, x2: { x_piece2}, count: {count}")
        

print(count)