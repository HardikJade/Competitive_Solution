a=int(input("Enter The No of Forces:  "))
x=[]
y=[]
z=[]
c=0
d=0
e=0
for i in range(0,a):
    b=int(input("Enter The Component:  "))
    c=c+b
    x.append(b)
    b=int(input("Enter The Component:  "))
    y.append(b)
    d=d+b
    b=int(input("Enter The Component:  "))
    e=e+b
    z.append(b)
if e==0 and d==0 and c==0:
    print("YES")
else:
    print("NO")