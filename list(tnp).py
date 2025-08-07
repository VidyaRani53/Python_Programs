m=list(map(int,input("enter numbers").split()))
evens=[(num,i) for i,num in enumerate(m) if num%2==0]
print(evens)
        
