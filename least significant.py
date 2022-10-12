"""
You should implement a function that takes as argument a positive integer xx and returns its least significant bit. 
More precisely you should return another integer whose binary representation contains a single bit set to 11, 
and that bit is the least significant one that is also set to 11 in xx.

Desired solution
Your function should work O(1)O(1) using bitwise operations.
"""

nums = int(input())

for x in range(nums):
    digit = int(input())
    digit = bin(digit)
    stringVal = str(digit)
    strRev = stringVal[::-1]
    
    for i in range(len(strRev)):
        if strRev[i] == '1':
            break

print(f'{2**i}')

