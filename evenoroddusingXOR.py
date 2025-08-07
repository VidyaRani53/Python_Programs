def isEven(n):
    if(n^1)==(n+1):
        return True
    else:
        return False
n=int(input())
if(isEven(n)==True):
    print("even")
else:
    print("odd")
