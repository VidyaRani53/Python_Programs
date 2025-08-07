'''take an input from the user and print the ouptut.
take odd position index elements square of each digit and store it in a string
and print 1st four digits.
Input1:34967   output:1636
Input2:14705    output:1600
n=input()
st=n[1::2]
otp=''
for i in st:
    otp+=str(int(i)**2).zfill(2)
print(otp[:4])'''
n=int(input())
s=str(n)
k=''
for i in range(len(s)):
    if i%2==0:
        continue
    else:
        k+=str(int(s[i])**2)
while(len(k)<4):
    k+='0'
print(k)
    
    
    
    
