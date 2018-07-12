import numpy as np
n=7
a = np.zeros((n,n))
i=0
m=n
x=0
while(i<n/2+1):
    for j in range(m):
        row=j+x
        if(i%2==0):
           a[row][j]=2
        else:
           a[row][j]=1
    x+=2
    i+=1
    m-=2
at=a.T
#combine the array
m=2*n-1
a1 = np.zeros((m,m))

#get values in first quaderent
for i in range(n):
    for j in range(n):
        a1[i][j+n-1]=a[i][j]

#get values in 2nd quaderent
for i in range(n):
    for j in range(n):
        a1[i+n-1][j]=at[i][j]

for i in range(m):
    for j in range(m):
        if(a1[i][j]==0):
            print(' ',end='')
        elif(a1[i][j]==2):
            print('x',end='')
        else:
            print('o',end='')
    print("")
            
