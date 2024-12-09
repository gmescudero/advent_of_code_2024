import copy as cp


equations = []
with open( "/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241207/data.txt") as f:
    for line in f:
        test,coeficients = line.strip().split(':')
        test = int(test)
        equations.append((test,tuple([int(c) for c in coeficients.strip().split(' ')])))


# operations = (lambda x,y: x+y, lambda x,y: x*y)
operations = (lambda x,y: x+y, lambda x,y: x*y, lambda x,y: int(str(x)+str(y)))


def recursive_operate(operands:tuple, coef:list, expected:int) -> bool:
    for op in operands:
        if len(coef) == 2:
                result = op(coef[0],coef[1])
                if result == expected: 
                    return True
        else:
            new_coef = list(cp.copy(coef))
            val = new_coef.pop(0)
            new_coef[0] = op(val,new_coef[0])
            if recursive_operate(operands, new_coef, expected): 
                return True
    return False



count = 0
for test,coeficients in equations:
    print(f"TEST:{test} coefs: {coeficients}")
    if recursive_operate(operations, coeficients, test):
        count += test

print(count)
