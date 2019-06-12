#DSA-Tryout

import sys

sys.setrecursionlimit(10000)   #This is to overcome default python recursion limit

def fibonacci(num):
    for i in range(3,num+1):
        memo[i]=memo[i-1]+memo[i-2]
    #Remove pass and write your logic here
    f=memo[num]
    return f
    pass

memo={1:1,2:1} #global dictionary to store the fibonacci number already computed
print("Fibonacci number:",fibonacci(5))
print("Fibonacci number:",fibonacci(10))
print("Fibonacci number:",fibonacci(30))
print("Fibonacci number:",fibonacci(35))
print("Fibonacci number:",fibonacci(40))
print("Fibonacci number:",fibonacci(50))
