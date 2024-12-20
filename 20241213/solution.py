from pprint import pprint
import copy as cp
from dataclasses import dataclass
import os
import re
from numpy import round

file_path = os.path.dirname(os.path.abspath(__file__))

@dataclass
class Equation2:
    a1:float
    a2:float
    b1:float
    b2:float
    c1:float
    c2:float

    def __repr__(self):
        return f"""
            {self.c1} = A*{self.a1} + B*{self.a2} 
            {self.c2} = A*{self.b1} + B*{self.b2} 
            """

    def solve(self):
        det = self.a1*self.b2 - self.a2*self.b1
        if det == 0:
            return None
        A = (self.b2*self.c1 - self.b1*self.c2) / det
        B = (self.a1*self.c2 - self.a2*self.c1) / det
        return A, B

    def tokens(self):
        A,B = self.solve()
        if A is None:
            return 0
        if A.is_integer() and B.is_integer():
            return A*3 + B
        return 0


equations = []  # List of Equation2 objects
text = None
with open(file_path +"/data.txt") as f:
    coefsA = None
    coefsB = None
    prizes = None
    for line in f:
        if line.startswith("Button A"):
            coefsA = [int(c) for c in re.findall(r"[0-9]+", line)]
        elif line.startswith("Button B"):
            coefsB = [int(c) for c in re.findall(r"[0-9]+", line)]
        elif line.startswith("Prize"):
            prizes = [int(c) for c in re.findall(r"[0-9]+", line)]
            equations.append(Equation2(coefsA[0],coefsA[1],coefsB[0],coefsB[1],10000000000000+prizes[0],10000000000000+prizes[1]))
            

total_tokens = 0
for eq in equations:
    total_tokens += eq.tokens()

print(int(total_tokens))

# Part 2
# Solution 401009100802023616 is too high