def cntUpper(li):
    for i in li:
        cnt=0
        for ch in i:
            if ch.isupper():
                cnt=cnt+1
        print(cnt)
n=int(input())
li=[]
for i in range(n):
    li.append(input())
cntUpper(li)
