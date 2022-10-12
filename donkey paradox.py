"""
On a field represented as a matrix of NN rows and MM columns there is a donkey and two haystacks.

The donkey is really hungry and he wants to get to a haystack as fast as possible. He can walk in four directions: up, down, left or right. The paradox of the donkey is that if the two haystacks are equally close to him he won't be able to decide which one to choose and he will starve to death.

You are given the cells of the haystackes, but you don't know where the donkey is. Compute the number of cells where the donkey will starve if he's there.

"""

field = input().split()
haystake1 = input().split()
haystake2 = input().split()
count = 0

for x in range(1,int(field[0])+1):
    for y in range(1,int(field[1])+1):
        if (abs(x-int(haystake1[0]))+abs(y-int(haystake1[1]))) == (abs(x-int(haystake2[0]))+abs(y-int(haystake2[1]))):
            count += 1
print(f'{count}')
