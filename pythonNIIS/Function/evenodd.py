#no return with no arrgument.
def oddeven():
	print("enter a number")
	no=int(input())
	if no%2==0:
		print("even number")
	else:
		print("odd number")
oddeven()

#odd even in return valu with arrgument.
def check(no):
	if no%2==0:
		print("even number")
	else:
		print("odd number")
print("enter a number")
no=int(input())
check(no)