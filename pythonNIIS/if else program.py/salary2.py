"""wep take emp salary from keybord if sak>=5000
da=30% hra=20% if sal<5000 da=20%,hra=10%
then display basic salary da hra and totalsal"""

print("enter basic salary")
sal=float(input())
da=sal*3 if sal>=5000 else sal*0.2
hra=sal*0.2 if sal>=5000 else sal*0.1
totalsal=sal+da+hra
print("badic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)