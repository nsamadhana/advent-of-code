#Day 3 Crossed Wires
#Find manhattan distance from central port to closest intersection of wires 
#manhattan distance = absolute difference of cartesian coordinates 
#Brute force: Calculate all intersection points and take minimum M.D 
#Mark each spot traveled (Indicate difference between line 1 and line 2)
#If mark already exists from other line, add the coordinate of intersection to the list and continue 
import sys
import math 

def stripOp(op):
    pair = []
    pair.append(op[0])
    pair.append(int(op[1:]))
    return pair

#Assumes origin is at (0,0)
def distance(p):
    return abs(p[0]-0) + abs(p[1]-0)

def findMin(points):
    minimum = sys.maxsize
    for each in points: 
        temp = distance(each)
        minimum = min(minimum,temp)
    return minimum 

#Returns the last coordinate it left off on 
def addLine(inst, p1, lSet1, lSet2, intersections):
    i = 1 
    op = inst[0] #L,R,U,D
    amount = inst[1] #How far to travel 
    if op == "U":
        while i < amount:
            if (p1[0], p1[1]+i) in lSet2: 
                intersections.append((p1[0], p1[1]+i))
            lSet1.add((p1[0], p1[1]+i))
            i += 1 
        p1[1] += i 
    elif op == "D":
        while i < amount:
            if (p1[0], p1[1]-i) in lSet2: 
                intersections.append((p1[0], p1[1]-i))
            lSet1.add((p1[0], p1[1]-i))
            i += 1 
        p1[1] -= i 
    elif op == "L":
        while i < amount:
            if (p1[0]-1, p1[1]) in lSet2: 
                intersections.append((p1[0]-1, p1[1]))
            lSet1.add((p1[0]-i, p1[1]))
            i += 1 
        p1[0] -= i 
    else: 
        assert op == "R" 
        while i < amount:
            if (p1[0]+1, p1[1]) in lSet2: 
                intersections.append((p1[0]+1, p1[1]))
            lSet1.add((p1[0]+i, p1[1]))
            i += 1 
        p1[0] += i 
    return(p1)

a = [x for x in open("input.txt").read().split("\n")]
l1 = a[0].split(",")
l2 = a[1].split(",")
l1Seen = set() 
l2Seen = set() 
curr = [0,0]
points = []

for each in l1: 
    op = stripOp(each)
    curr = addLine(op, curr, l1Seen, l2Seen, points)
curr = [0,0]
for each in l2:
    op = stripOp(each)
    curr = addLine(op, curr, l2Seen, l1Seen, points) 
print(findMin(points))



    
    

    




