# from pprint import pprint
import copy as cp
import numpy as np
import time as t
# import threading as th
import concurrent.futures

st_time = t.time()

# text = "70949 6183 4 3825336 613971 0 15 182"
text = "70949"
blinks_num = 75

# text = "125 17"
# blinks_num = 25

# 0 -> 1
# even digits -> split: the left gets the left sided digits and the right the rest
# else -> mulitply by 2024

def blink_stone_times(stone:int, blinks_num:int):
    stones = [stone]
    for i in range(blinks_num):
        new_stones = []
        for st in stones:
            digits_num = len(str(st))
            if st == 0:
                new_stones.append(1)
            elif digits_num % 2 == 0:
                pivot = 10**(digits_num/2)
                # pivot = np.pow(10,digits_num/2)
                left_value  = int(st/pivot)
                right_value = int(st - left_value*pivot)
                new_stones.append(left_value)
                new_stones.append(right_value)
            else:
                new_stones.append(st*2024)
        stones = cp.deepcopy(new_stones)
        # print(f"{stones}")
        print(f"[{t.time()-st_time}] Progress in thread {i}/{blinks_num}")
    return stones


def blinks(current_stones:list, blinks_num:int):
    stones = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for st in current_stones:
            futures.append(executor.submit(blink_stone_times,st,blinks_num))
        for futu in futures:
            stones += futu.result()
            print(f"[{t.time()-st_time}]\t -> Finished {len(stones)}")
    return stones

stones = [int(c) for c in text.strip().split(' ')]
print(len(blinks(stones,blinks_num)))


