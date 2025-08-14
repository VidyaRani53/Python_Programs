'''segregate the given elements first all even elements in descending oreder and
all the odd elements in ascedingorder'''
li=list(map(int,input().split()))
even=[]
odd=[]
output=[]
for i in range(len(li)):
    if li[i]%2==0:
        even.append(li[i])
    else:
        odd.append(li[i])
for i in range(len(even)):
    output.append(max(even))
    even.remove(max(even))
for i in range(len(odd)):
    output.append(min(odd))
    odd.remove(min(odd))
print(output)
    

    
