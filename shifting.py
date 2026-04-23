#program to rotate an array n times to the right
'''input = [1,2,3,4,5]
rotate = 2
output = [4,5,1,2,3]
1. reverse the entire array
2. reverse first rotate elements
3. reverse remaining elements'''

'''def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
arr = list(map(int,input().split()))
k = int(input("enter the rotation:"))
n = len(arr)
k = k%n
reverse(arr,0,n-1)
reverse(arr,0,k-1)
reverse(arr,k,n-1)
print(arr)'''

#program to rotate an n times to the left
'''def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start+=1
        end-=1
arr = list(map(int,input().split()))
k = int(input("enter the rotation:"))
n = len(arr)
k = k%n
reverse(arr,0,k-1)
reverse(arr,k,n-1)
reverse(arr,0,n-1)
print(arr)'''

#to rotate 2d array with 90 degree clockwise mode
'''row = int(input("enter num of rows: "))
cols = int(input("enter num of cols: "))
matrix = []
print("Enter matrix row wise:")
for i in range(row):
    rows = list(map(int,input().split()))
    matrix.append(rows)
for i in range(row):
    for j in range(i,cols):
        matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
for i in range(row):
    matrix[i].reverse()
print("90 degrees clockwise matrix:")
for row in matrix:
    print(*row)'''

#to rotate 2d array with 90 degree anti clockwise mode
row = int(input("enter num of rows: "))
cols = int(input("enter num of cols: "))
matrix = []
print("Enter matrix row wise:")
for i in range(row):
    rows = list(map(int,input().split()))
    matrix.append(rows)
for i in range(row):
    for j in range(i,cols):
        matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
for i in range(cols):
    matrix.reverse()
print("90 degrees anti clockwise matrix:")
for row in matrix:
    print(*row)




















