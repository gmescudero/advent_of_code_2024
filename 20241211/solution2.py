# from pprint import pprint
import copy as cp
import numpy as np
import time as t
# import threading as th
# import concurrent.futures

st_time = t.time()

text = "70949 6183 4 3825336 613971 0 15 182"
# text = "70949"
blinks_num = 75

# text = "125 17"
# blinks_num = 25


stones = [int(c) for c in text.strip().split(' ')]
stones_dict = {}
for st in stones:
    if st in stones_dict:
        stones_dict[st] += 1
    else:
        stones_dict.update({st:1})

def blink_stone(stone:int) -> list:
    new_stones = []
    digits_num = len(str(stone))
    if stone == 0:
        new_stones.append(1)
    elif digits_num % 2 == 0:
        pivot = 10**(digits_num/2)
        # pivot = np.pow(10,digits_num/2)
        left_value  = int(stone/pivot)
        right_value = int(stone - left_value*pivot)
        new_stones.append(left_value)
        new_stones.append(right_value)
    else:
        new_stones.append(stone*2024)
    return new_stones

for i in range(blinks_num):
    new_stones_dict = {}
    for st,st_num in stones_dict.items():
        new_stones = blink_stone(st)
        for new_st in new_stones:
            if new_st in new_stones_dict:
                new_stones_dict[new_st] += st_num
            else:
                new_stones_dict.update({new_st:st_num})
    stones_dict = cp.deepcopy(new_stones_dict)
    print(f"[{t.time()-st_time:.4f}] Blinked {i+1} times out of {blinks_num}")

count = 0
for st_num in stones_dict.values():
    count += st_num

print(f"[{t.time()-st_time:.4f}] Total number of stones: {count}")

