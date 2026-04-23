'''traversal of 2D array
                top
             1  2 3  4 
    left    12 13 14 5   right
            11 16 15 6
            10  9 8  7

               bottom '''

'''n = int(input())
matrix = [[0]*n for _ in range(n)]
top = 0
bottom = n-1
left = 0
right = n-1
num =1 
while top<=bottom and left<=right:
    #left->right(top)
    for i in range(left,right+1):
        matrix[top][i]=num
        num+=1
    top+=1
    #top->botttom(right)
    for i in range(top,bottom+1):
        matrix[i][right]=num
        num+=1
    right-=1
    #right->left(bottom)
    for i in range(right,left-1,-1):
        matrix[bottom][i]=num
        num+=1
    bottom-=1
    #bottom->top(left)
    for i in range(bottom,top-1,-1):
        matrix[i][left]=num
        num+=1
    left+=1
print("spiral pattern clock wise:")
for row in matrix:
    print(*row)'''


#transversal of a matrix(2D array) in a spiral clock wise roration
rows = int(input())
cols = int(input())
matrix = []
print("enter matrix elements : ")
for i in range(rows):
    row = list(map(int,input().split()))
    matrix.append(row)
top = 0
bottom = rows - 1
left = 0
right = cols - 1
print("spiral traversal of a matrix:")
while top<=bottom and left<=right:
    for i in range(left,right+1):
        print(matrix[top][i], end = '')
        top+=1
    for i in range(top,bottom-1):
        print(matrix[i][right], end = '')
        right-=1
    for i in range(right,left-1,-1):
        print(matrix[i][bottom])
        bottom-=1
    if left <= right:
        for i in range(bottom,top-1,-1):
            print(matrix[i][left],end = '')
        left +=1

