# --> Write a program to count the number of even and odd numbers from a series of numbers. 
# -> Sample : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# -> Number of even numbers: 5 
# -> Number of odd numbers: 4

# Input Format
# 4 1 2 3 4

# Output Format
# 2 -> even count 
# 2 -> odd count


n=int(input())
even=[]
odd=[]
for i in range(0,n):
    num=int(input())
    if(num%2==0):
        even.append(num)
    else:
        odd.append(num)
        
print(len(even))
print(len(odd))
