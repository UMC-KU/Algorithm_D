# 미완 - **빗물
import sys
def rain(start):
    global blocks, w
    water = 0
    end = -1
    index = start
    while index < w:
        if blocks[index] > blocks[start] or or (index + 1 == w and blocks[index] > blocks[index-1]):
            end = index
            point = min(blocks[end], blocks[start])
            for i in range(start, end):
                water += blocks[point] - blocks[i]
            break
        index += 1
    return water

h, w = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))
water = 0
index = 0   # current index
while index < w:
    if blocks[index] > blocks[index+1]:
        water += rain(index)
    index += 1
print(water)