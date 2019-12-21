#Day 1 Tyranny of the Rocket 

import math
of = open("input.txt", "r")


def main():
    totalFuel = 0  
    for line in of:
        totalFuel += fof(int(line))
    of.close()
    print(totalFuel)
    return totalFuel


#Take floor of division by 3 and subtract by 2
def fuelReq(val):
    return math.floor(val/3) - 2 

def fof(val):
    totalFuel = 0 
    while(fuelReq(val) > 0):
        val  = fuelReq(val)
        totalFuel += val  
    return totalFuel 
     

if __name__ == "__main__": 
    main()