l=[3,1,2,4,5,6]
n=len(l)
for i in range(n//2):
    l[i],l[n-i-1]=l[n-i-1],l[i]
print(*l)
