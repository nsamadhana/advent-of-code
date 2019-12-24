#Day 4 Secure Container 
#Input range: 231832-767346
'''
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; 
they only ever increase or stay the same (like 111123 or 135679)
'''
#Part 2: Adjacent pair cannot be part of a larger group of numbers 
#Check if there exists at least one double pair 

def isPair(a):
    for i in range(1,len(a)-1):
        if a[i]==a[i+1] or a[i]==a[i-1]: 
            return True
    return False 

def isDouble(a):
    for i in range(len(a)): 
        if a.count(a[i]) == 2: 
            return True 
    return False 
    

def isIncreasing(a):
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            return False
    return True 

lb = 231832
rb = 767346
count = 0 
while lb < rb: 
    if isIncreasing(str(lb)) and isDouble(str(lb)):
        print(lb)
        count += 1 
    lb += 1 
print(count)
