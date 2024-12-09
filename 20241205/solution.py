
from math import floor
import json


rules = {}
updates = []
with open("/home/gmoreno/Workspace/pruebas/adventOfCode2024/20241205/data.txt") as f:
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

# import itertools
# all_numbers = itertools.permutations([97,75,61,53,47,29,13])
# updates = list(all_numbers)
# print(updates)


print(f"RULES: \n{json.dumps(rules,indent=4,sort_keys=True)}\n\n")

count = 0

for updt in updates:
    correct = True
    updt = list(updt)
    # print(f"{updt}\t=> ",end="")
    for rule,pages in rules.items():
        if rule in updt:
            for page in pages:
                if page in updt: 
                    rule_idx = updt.index(rule)
                    page_idx = updt.index(page)
                    if rule_idx > page_idx:
                        updt.pop(rule_idx)
                        updt.insert(page_idx,rule)
                        correct = False
    if not correct: count += updt[floor(len(updt)/2)]

print(count)
