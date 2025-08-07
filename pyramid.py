'''write a program to print pyramid pattern
        *
       * *
      * * *
     * * * *
    * * * * *
    '''
n=int(input())
for i in range(n):
    for j in range(0,n-i-1):
        print(end=' ')
    for k in range(0,i+1):
        print('*',end=' ')
    print()
