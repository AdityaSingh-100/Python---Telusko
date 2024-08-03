# 1) Write a program to find prime numbers to check number is prime or not

x = int(input("Enter a number: "))

if x > 1:
    for i in range(2,x):
        if x%i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")