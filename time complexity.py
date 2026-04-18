#program to fetch a value from an array for content optimization
'''def value(arr):
    return arr[-3]

arr = list(map(int,input("enter elements: ").split()))
print(value(arr))'''

'''def value(arr):
    for i in arr:
        print(i-10, end = ' ')
arr = list(map(int,input("enter elements: ").split())
value(arr)'''

#program to fetch a value from an array for nested (quadratic optimization)
'''def pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i],arr[j])
arr = list(map(int,input("Enter elements: ").split()))
pairs(arr)'''

#program to find the steps pf exponential format of a given number where logarthemic reflects
def power(x,n):
    result = 1
    steps = 0
    while n != 0:
        steps += 1
        print(f"steps = {steps}: x = {x},n = {n}, result = {result}")
        if n%2 == 1:
            result *= x
        x*= x
        n//=2 
    print(f"final result : {result}")
    print(f"Total Steps: {steps}")
base = int(input())
expo = int(input())
power(base,expo)


















