#PROGRAM 11: Quotient and Remainder
#Write a Python program to find quotient and remainder.
print("enter first number")
a = int(input())

print("enter second number")
b = int(input())

if b == 0:
    print("Division by zero is not allowed")
else:
    q = a // b
    r = a % b
    print("quotient =", q)
    print("remainder =", r)