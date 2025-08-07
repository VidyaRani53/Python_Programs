'''Take an input from the user in the format of name and code.firstly find the maximum digit from the code
which is less than or equal to length of the name and place that position character
in a final string.If this condition doesn'tsatisfied then simply put X.
Input:abhishek:34848,mayur:4789,friend:23578,yeah:9889
output: kunX'''
a=input().split(',')
output=''
for i in a:
    temp=i.split(':')
    name=temp[0]
    code=temp[1]
    max=0
    l=len(name)
    for digit in code:
        if (int(digit)<=l):
            if (max<int(digit)):
                max=int(digit)
    if(max==0):
        output+='X'
    else:
        output+=name[max-1]
print(output)
