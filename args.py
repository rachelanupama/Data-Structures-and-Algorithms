#no args no return value
def hi():
    print("hello", end = '')
    print("how are u")
hi()

#arg pass no return value








#no arg and pass return value
def num():
    return 100
x = num()
print(x)

#arg pass and return value
def summate(a,b):
    return a+b

num1 = int(input())
num2 = int(input())
result = summate(num1,num2)
print(result)

#multiple args and multiple returns
def info(name,age):
    return name,age
n = input("name:")
a = int(input("age:"))
n,a = info(n,a)
print(n,a)
