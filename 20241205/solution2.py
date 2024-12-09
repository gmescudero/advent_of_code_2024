rules = {}
updates = []
with open("/home/gmoreno/Workspace/pruebas/advent_of_code_2024/20241205/data.txt") as f:
    for l in f.readlines():
        if '|' in l:
            rule = [int(c) for c in l.strip().split('|')]
            # print(rule)
            if rule[0] in rules:
                # print(rules[rule[0]])
                rules[rule[0]] = rules[rule[0]] + [rule[1]]
            else:
                rules.update({rule[0]:[rule[1]]})
        elif ',' in l:
            updates.append([int(c) for c in l.strip().split(',')])



# for every update 
for updt in updates:
    # for every page in the update list
    for i,updt_page in range(len(updt)-2,0,-1):
        # 
        new_index = i
        for rule in rules:
            if updt_page == rule[0] and rule[1] in updt:
                index = updt.index(rule[1])
                if index > new_index:
