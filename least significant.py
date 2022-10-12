"""
You should implement a function that takes as argument a positive integer xx and returns its least significant bit. 
More precisely you should return another integer whose binary representation contains a single bit set to 11, 
and that bit is the least significant one that is also set to 11 in xx.

Desired solution
Your function should work O(1)O(1) using bitwise operations.
"""
# Parameter x is an integer
# The function should return an integer
def lsb(x):
    x = bin(x)
    stringVal = str(x)
    strRev = stringVal[::-1]
    
    for i in range(len(strRev)):
        if strRev[i] == '1':
            break
    return 2**i
###
tests = int(input())
for i in range(tests):
    x = int(input())
    answer = lsb(x)
    print(answer)


