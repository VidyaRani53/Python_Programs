import math as m
n=int(input())
k=n
l=len(str(n))
sum=0
while n>0:
    sum+=m.pow(n%10,l)
    n//=10
if sum==k:
    print("armstrong")
else:
    print("not armstrong")
    
    
