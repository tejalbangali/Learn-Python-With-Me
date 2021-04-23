# Performing Operations:
a=10
b=5

print(a + b)   #Addition
print(a - b)   #Subtraction
print(a * b)   #Multiplication
print(a / b)   #True Division
print(a // b)  #Floor Division
print(a % b)   #Modulus
print(a ** b)  #Exponentiation
print(-a)


# Loops
for n in range(1, 10):     #for loop
    print(n)
    
    
while n<10:                #while loop
    print(n)
    n += 1
 

# Conditional Statements
if(x == 1):
    print('a')
elif(x == 2):
    print('b')
else:
    print('c')
    
    
#Ternary Operator
x='a' if n>1 else 'b'


#Chaining comparison operators 
if 18<= age <65:
    
    
#Type conversion
int(x)
float(x)
bool(x)
str(x)


#Falsy values
0
""
[]


#Functions 
def increment(number, by=1):
    return number + by
    
    
#Keyword Arguments 
increment(2, by=1)


#Variable number of arguements 
def multiply(*numbers):
    for number in numbers:
        print(number)

multiply(1,2,3,4,5)


#Variable number of keyword argument
def save_user(**user):
    ....
    
save_user(id=1, name='Tejal')


#Strings
x = 'Python'
len(x)
x[0]
x[-1]
x[0:3]


#Formatted Strings
name = f"{first} {last}"


#Escape Sequences
\"
\'
\\
\n


#String Methods
x.upper()
x.lower()
x.title()
x.strip()
x.find('p')
x.replace('a','b')
'a' in x
