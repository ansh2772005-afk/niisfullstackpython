#swapping using 3rd veriable 
a=10
b=20
print("before swaping a=",a,"b=",b)
t=a 
a=b
b=t 
print("after swaping a=",a,"b=",b)
#swapping without using 3rd veriable 
a=10
b=20
print("before swaping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("after swaping a=",a,"b=",b)
#tuple class
a=10,2.5,"hii" 
print(a)
print(type(a))
print(id(a))
#swapping in python
a=10
b=20
a,b=b,a
print(a,b)
#swapping 3 value using 4th variable
a=10
b=20
c=30
print("before swaping a=",a,"b=",b,"c=",c)
t=c 
b=c 
c=a 
a=t  
print("after swaping a=",a,"b=",b,"c=",c)