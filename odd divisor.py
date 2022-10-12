"""
You are given an interval of integers [A, B][A,B]. For each number in this interval compute its greatest odd divisor. Output the sum of these divisors.

Standard input
The first line contains an integer TT representing the number of test cases that will follow.

Each test case consists of one line containing two integer values AA and BB.

Standard output
The output should contain the answer for each test case on a different line.

Each answer consists of a single integer value.

"""

nums = int(input())
for x in range(nums):
    m = input().split()
    sum_of_div:int = 0
    for i in range(int(m[0]),int(m[1])+1):
        max_div:int = 1
        for x in range(1,i+1):
            if (i%x==0) and ( x%2 == 1 ):
                max_div = x
        sum_of_div += max_div
    print(f"{sum_of_div}")
