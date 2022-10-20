r1 = ['0,0','1,0','2,0','3,0','4,0']
r2 = ['0,1','1,1','2,1','3,1','4,1']
c1 = ['0,0','0,1','0,2','0,3','0,4']
c2 = ['1,0','1,1','1,2','1,3','1,4']

board_size =int(input('Enter board size: '))
w_arr=[]
b_arr=[]
count = 0
# Capturing the coordinates
for i in range(6):
    coordinate = input('Enter coordinate: ')

    if count%2==0:
        b_arr.append(coordinate)
    else:
        w_arr.append(coordinate)
    count+=1
# Comparing the coordinates with database.abs
count_c1=0
count_c2=0
count_r1=0
count_r2=0
for i in b_arr:
    if i in c1:
        count_c1+=1
    if i in c2:
        count_c2+=1
    if i in r1:
        count_r1+=1
    if i in r2:
        count_r2+=1
c_max = max(count_c1, count_c2)
r_max = max(count_r1, count_r2)
print(b_arr)
print(w_arr)
if (max(c_max, r_max)+2)==5:
    print(1)
else:
    print(0)






