"""
You are given an integer NNN that can be represented on 323232 bits. 
Implement a function that counts the numbers of bits set to 111 in NNN's binary representation. 
"""


# Parameter x is an integer
# The function should return an integer
def bitcount(x):
    x  = str(f'{x:08b}')
    count = 0
    for i in x:
        if i == "1":
            count += 1
    return count
    
x = int(input())
print(bitcount(x))
