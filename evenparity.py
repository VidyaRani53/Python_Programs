s=input("enter a string with 0's and 1's")
n=list(s)
n1=n.count('1')
if(n1%2==0):
    n.append('0')
else:
    n.append('1')
print("after appending even parity bit")
print(''.join(n))
