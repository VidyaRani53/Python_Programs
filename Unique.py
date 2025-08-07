def Unique(str):
    s=set()
    for i in range(len(str)):
        s.add(str[i])
    return len(s)
str=input()
print(Unique(str))
