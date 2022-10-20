first = input("Enter Rectangle Dimensions").split()
second = input("Number of red Diameter of red ").split()
third = input("Number of green Diameter of green").split()

# testing
count =0
area = 0
while area < int(first[0]):
    if count%2==0:
        area+=int(second[1])
    else: 
        area+=int(third[1])
    count+=1
print(count)
