from pprint import pprint
import copy as cp


text = "70949 6183 4 3825336 613971 0 15 182"
blinks_num = 75

# text = "125 17"
# blinks_num = 25

# 0 -> 1
# even digits -> split: the left gets the left sided digits and the right the rest
# else -> mulitply by 2024

def digitize(n):
  return list(map(int, str(n)))

def de_digitize(n:list):
  num = 0
  for i,d in enumerate(n[::-1]):
    num += (10**i) *d
  return num

def blink(current_stones:list):
    stones = []
    for st in current_stones:
        digits_num = len(str(st))
        if st == 0:
            stones.append(1)
        elif digits_num % 2 == 0:
            pivot = 10**(digits_num/2)
            left_value  = int(st/pivot)
            right_value = int(st - left_value*pivot)
            stones.append(left_value)
            stones.append(right_value)
        else:
            stones.append(st*2024)
    return stones

stones = [int(c) for c in text.strip().split(' ')]

for i in range(blinks_num):
    # print(stones)
    print(f"Blinking for the {i+1}th times out of {blinks_num}")
    stones = blink(stones)


# print(stones)
print(len(stones))
