#Day 3 Crossed Wires
#Find manhattan distance from central port to closest intersection of wires 
#manhattan distance = absolute difference of cartesian coordinates 
#Brute force: Calculate all intersection points and take minimum M.D 
#Mark each spot traveled (Indicate difference between line 1 and line 2)
#If mark already exists from other line, add the coordinate of intersection to the list and continue 
#Part 2: Return the minimum number of steps taken by both wires to reach an intersection (R8 = 8 steps)
#Each step coordinate should maintain the number of steps that it took to get there 
#

import math
import sys

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
    nSteps = 0
    steps = {} 
    seen = set()
    for each in arr: 
        temp = stripOp(each)
        d = temp[0]
        n = temp[1]
        for i in range(n):
            x += dx[d]
            y += dy[d]
            nSteps += 1
            steps.update({(x,y) : nSteps})
            seen.add((x,y))
    return (seen, steps)


a = [x for x in open("input.txt").read().split("\n")]
l1 = a[0].split(",")
l2 = a[1].split(",")

p1 = points(l1)
p2 = points(l2)
intersections = p1[0] & p2[0]
#Take the minimum sum of steps for all intersections 
minSteps = sys.maxsize
for i in intersections: 
    steps = p1[1][i] + p2[1][i]
    minSteps = min(steps, minSteps)
print(minSteps)
    








    
    

    




