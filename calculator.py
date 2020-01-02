import sys;

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def div(x,y):
    z = x / y
    return z
    #if y==0:
        #print("Division by Zero not allowed")
    #else:


print("Select any operation: \n")
print("1. Addition \n 2. Subtraction \n 3. Mutiplication \n 4. Division \n")

select1=input("Enter your choice(1/2/3/4): ")

num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

if select1=='1':
    print("Addition of 2 nos. is:",add(num1,num2))
elif select1=='2':
    print("Subtraction of 2 nos. is:", sub(num1, num2))
elif select1=='3':
    print("Multiplication of 2 nos. is:", multiply(num1, num2))
elif select1=='4':
    if num2==0:
        print("Division by 0 is not allowed.")
    else:
        print("Division of 2 nos. is:", div(num1, num2))
else :
   print("Wrong selection. This operation does not exist.")
