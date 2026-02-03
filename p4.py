# write a program to print the factorial of given number.

n = int(input("Enter number"))
sum = 1
for i in range(1,n+1):
    sum = sum*i
    print(sum)