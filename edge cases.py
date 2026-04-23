#reverse of an array - empty,duplicate
'''arr = list(map(int,input().split()))
if len(arr)==0:
    print("Empty")
else:
    left,right = 0,len(arr)-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
print(arr)'''

#palindrome

'''s = input("String:")
if s =='':
    print("String empty")
else:
    if s == s[::-1]:
        print("is a palindrome")
    else:
        print("Not a palindrome")'''

#move all the zeroes to the end of array
'''arr = list(map(int,input("enter elements:").split()))
pos = 0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos+=1
print(arr)'''

#find all the first non repeating element
'''arr = list(map(int,input().split()))
if len(arr)==0:
    print("array empty")
else:
    found = False
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count+=1
        if count==1:
            print("first non repeating number:", arr[i])
            found = True
            break
    if not found:
        print("no non repeating number")'''

#anagram
'''1. Harry potter
2. try hero part

cases:
1. case
2. length difference
3. sorted
4. "" == ""'''

s1 = input("s1:").strip().lower().replace(' ','')
s2 = input("s2:").strip().lower().replace(' ','')
if len(s1) == 0 and len(s2):
    print("Both the arrays are empty")
elif len(s1) == 0 or len(s2) == 0:
    print("one of the array is empty")
elif len(s1)!=len(s2):
    print("Not an anagram")
elif sorted(s1) == sorted(s2):
    print("They are anagrams")

