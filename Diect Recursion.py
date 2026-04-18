'''def natural():
    if num == 0:
        return
    print(num, end = '')
    natural(num-1)

num = int(input("enter a num:"))
natural(num)'''

#factorial
'''def fact(num):
    if num == 0 or num == 1:
        return 1
    return num * fact(num-1)
num = int(input())
output = fact(num)
print(output)'''

#even or odd
'''def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n-1)
    
def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n-1)
num = int(input("Enter a number:"))
if is_even(num):
    print(num,"is even number")
else:
    print(num,"is odd number")'''

#indirect recursion of a factorial

def one(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*two(n-1)
def two(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n *one(n-1)
num = int()

































