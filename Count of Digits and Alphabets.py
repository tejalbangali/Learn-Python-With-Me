# --> Write a program that accepts a string and calculates the number of digits and letters. 

# -> Input Format: Python 3.2

# -> Output Format: 
# 6 = letter count 
# 2 = digit count


word= input()
alph=dig=0

for i in word:
    if(i.isdigit()):
        dig=dig+1
    
    elif(i.isalpha()):
        alph=alph+1
        
    else:
        pass
    
print(alph)
print(dig)
