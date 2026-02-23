# PROGRAM 14: Compound Interest
#Write a Python program to calculate compound interest. PROGRAM 14: Compound Interest
print("enter principal")
P = float(input())

print("enter rate (in %)")
r = float(input()) / 100   # convert percentage to decimal

print("enter time")
t = float(input())

print("enter number of times compounded")
n = int(input())

CI = P * (1 + r/n) ** (n*t) - P

print("compound interest =", CI)