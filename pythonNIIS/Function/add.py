def add():
	print("Enter 1st no")
	num1=int(input())
	print("Enter 2nd no")
	num2=int(input())
	s=num1+num2
	print("sum=",s)
add() 

#return value with argument   add two number 

def add(no1,no2):
	s=no1+no2
	return s
print("enter a number ")
no1=int(input())
print("enter another number ")
no2=int(input())
res=add(no1,no2)
print("sum=",res)


