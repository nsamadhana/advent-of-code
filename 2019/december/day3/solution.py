#Day 3 Crossed Wires
#Find manhattan distance from central port to closest intersection of wires 
#manhattan distance = absolute difference of cartesian coordinates 
#Brute force: Calculate all intersection points and take minimum M.D 
#Mark each spot traveled (Indicate difference between line 1 and line 2)
#If mark already exists from other line, add the coordinate of intersection to the list and continue 
#Part 2: Return the minimum number of steps taken by both wires to reach an intersection (R8 = 8 steps)

import sys
import math

dy = {"L":0, "U":1, "R":0, "D":-1}
dx = {"L":-1, "U":0, "R":1, "D":0}

def stripOp(op):
    pair = []
    pair.append(op[0])
    pair.append(int(op[1:]))
    return pair

def findMin(points):
    temp = min(points)
    return(abs(temp[0])+abs(temp[1]))

def points(arr):
    x = 0 
    y = 0 
    seen = set()
    for each in arr: 
        temp = stripOp(each)
        d = temp[0]
        n = temp[1]
        for i in range(n):
            x += dx[d]
            y += dy[d]
            seen.add((x,y))
    return seen


a = [x for x in open("input.txt").read().split("\n")]
l1 = a[0].split(",")
l2 = a[1].split(",")
intersections = points(l1) & points(l2)
closest = min(intersections)
print(abs(closest[0]) + abs(closest[1]))


    
    

    




