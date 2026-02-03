# write a program to print prime number series between 1 to 50.


def is_prime(n):
    if n<=1:
        return False
    for i in range(1,n):
        if n%2==0:
            return False
        return True
for n in range(1,50):
    if is_prime(n):
        print(n)
        