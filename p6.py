# Write a program to print the largest number between 3 numbers using nested if-else.

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

if(num1>num2):
    if(num1>num3):
        print("Biggest number is: ",num1)
    else:
        print("Biggest number is: ",num3)
else:
    if(num2>num3):
        print("Biggest number is:",num2)
    else:
        print("Biggest number is:",num3)
    
