"""wep take emp salary from keybord if sak>=5000
da=30% hra=20%
then display basic salary da hra and totalsal"""

print("enter basic salary")
sal=float(input())
da,har=0,0
if sal>=5000:
  da=sal*0.3
  hra=sal*0.2
totalsal=sal+da+har
print("badic sal=",sal)
print("da=",da)
print("har=",hra)
print("total salary=",totalsal)