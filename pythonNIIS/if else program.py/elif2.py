#wap take no from keyboard check no is sd dd  td and od using elif .
print("enter a number")
no=int(input())
if no<10:
    print("number is sd")
elif no<100:
	print("number is dd")
elif no<1000:
	print("number is td")
elif no>1000:
	print("number is od")
else:
	print("number is +ve")
