def bit_removal(x, y):
    return x^(x&y)
    
###
tests = int(input())
for test in range(tests):
    x, y = map(int, input().split(' '))
    answer = bit_removal(x, y)
    print(answer)
