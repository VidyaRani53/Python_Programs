n=int(input())
for i in range(2,11):
    num=n*i
    k=num
    sum=0
    while(num>0):`
        sum=sum+num%10
        num//=10
    if sum==n:
        print(k)
        break
