def a1(a,b,i,j):
    if b%2==0:
        a[i][j]=a[i][j]
    elif b%2!=0:
        if a==0:
            a[i][j]=1
        else:
            a[i][j]=0
def a2(a,b,i,j):
    if b%2==0:
        a[i][j]=a[i][j]
    elif b%2!=0:
        if a==0:
            a[i][j]=1
        else:
            a[i][j]=0
def a3(a,b,i,j):
    if b%2==0:
        a[i][j]=a[i][j]
    elif b%2!=0:
        if a==0:
            a[i][j]=1
        else:
            a[i][j]=0
def b1(a,b,i,j):
    if b%2==0:
        a[i][j]=a[i][j]
    elif b%2!=0:
        if a==0:
            a[i][j]=1
        else:
            a[i][j]=0
def b2(a,b,i,j):
    if b%2==0:
        a[i][j]=a[i][j]
    elif b%2!=0:
        if a==0:
            a[i][j]=1
        else:
            a[i][j]=0
def b3(a,b,i,j):
    if b%2==0:
        a[i][j]=a[i][j]
    elif b%2!=0:
        if a==0:
            a[i][j]=1
        else:
            a[i][j]=0
def c1(a,b,i,j):
    if b%2==0:
        a[i][j]=a[i][j]
    elif b%2!=0:
        if a==0:
            a[i][j]=1
        else:
            a[i][j]=0
def c2(a,b,i,j):
    if b%2==0:
        a[i][j]=a[i][j]
    elif b%2!=0:
        if a==0:
            a[i][j]=1
        else:
            a[i][j]=0
def c3(a,b,i,j):
    if b%2==0:
        a[i][j]=a[i][j]
    elif b%2!=0:
        if a==0:
            a[i][j]=1
        else:
            a[i][j]=0
a=[[1,1,1],[1,1,1],[1,1,1]]
b=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        c=int(input("Enter The No:  "))
        b[i][j]=c
# For a[0][0]
a1(a[0][0],b[0][0],0,0)
a2(a[0][1],b[0][1],0,1)
b1(a[1][0],b[1][0],1,0)
b2(a[1][1],b[1][1],1,1)

#For a[0][1]
a1(a[0][0],b[0][0],0,0)
a2(a[0][1],b[0][1],0,1)
a3(a[0][2],b[0][2],0,2)
b1(a[1][0],b[1][0],1,0)
b2(a[1][1],b[1][1],1,1)
b3(a[1][2],b[1][2],1,2)

#For a[0][2]
a2(a[0][1],b[0][1],0,1)
a3(a[0][2],b[0][2],0,2)
b2(a[1][1],b[1][1],1,1)
b3(a[1][2],b[1][2],1,2)

#For b[0][1]
a1(a[0][0],b[0][0],0,0)
a2(a[0][1],b[0][1],0,1)
b1(a[1][0],b[1][0],1,0)
b2(a[1][1],b[1][1],1,1)
c1(a[2][0],b[2][0],2,0)
c2(a[2][1],b[2][1],2,1)

#For b[0][2]
a2(a[0][1],b[0][1],0,1)
a3(a[0][2],b[0][2],0,2)
b2(a[1][1],b[1][1],1,1)
b3(a[1][2],b[1][2],1,2)
c2(a[2][1],b[2][1],2,1)
c3(a[2][2],b[2][2],2,2)

#For c[0][0]
b1(a[1][0],b[1][0],1,0)
b2(a[1][1],b[1][1],1,1)
c1(a[2][0],b[2][0],2,0)
c2(a[2][2],b[2][2],2,2)

#For c[0][1]
b1(a[1][0],b[1][0],1,0)
b2(a[1][1],b[1][1],1,1)
b3(a[1][2],b[1][2],1,2)
c1(a[2][0],b[2][0],2,0)
c2(a[2][1],b[2][1],2,1)
c3(a[2][2],b[2][2],2,2)

#For c[0][2]
b2(a[1][1],b[1][1],1,1)
b3(a[1][2],b[1][2],1,2)
c2(a[2][1],b[2][1],2,1)
c3(a[2][2],b[2][2],2,2)

