import math 
#Day 2 1202 Program Alert 
#Target is 19690720
nums = [int(x) for x in open("input.txt").read().split(",")]
target = 19690720

def main():
    for x in range(100):
        for y in range(100):
            a = [x for x in nums] #Copies original list 
            a[1] = x 
            a[2] = y
            i = 0 
            while(True):
                opcode = a[i]
                i1,i2,i3 = a[i+1], a[i+2], a[i+3]
                if opcode == 1: 
                    a[i3] = a[i1] + a[i2]
                elif opcode == 2:
                    a[i3] = a[i1] * a[i2]
                else:
                    assert opcode == 99 
                    break 
                i += 4
            if a[0] == target:
                print(x, y)
                break

    

if __name__ == "__main__": 
    main()