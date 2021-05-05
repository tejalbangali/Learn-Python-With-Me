# --> Write a program to get the number of occurrences of a specified element in an array.

# -> Input Format: 3 7 1 3 5 3 7 9 3
# -> Constraints: the first number is the specified element the second number length of the array. and remaining are the array integers.

# -> Output Format: 3


find=int(input())
length=int(input())
li=[]

for i in range(0,length):
    add=int(input())
    li.append(add)

    count=0

for i in range(0,length):
    if(li[i] is find):
        count=count+1
print(count)
