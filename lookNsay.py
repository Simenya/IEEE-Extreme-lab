# Parameter n is an integer
# The function should return a string
def look_and_say(n):
    

    if n == 1:
        result = '1'
    
    elif n == 2:
        result = '11'
    
    else:
        sample = '11'
        for x in range(3,n+1):
            count = 1
            sample +="@"
            temp = ""
    
            for i in range(1,len(sample)):
                if sample[i] != sample[i-1]:
                    temp += str(count)
                    temp += sample[i-1]
                    count = 1
                
                else:
                    count += 1
            sample = temp
        return f"{sample}"

###
n = int(input())
answer = look_and_say(n)
print(answer)
