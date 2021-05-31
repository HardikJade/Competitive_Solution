a=int(input("Enter The No of Students:  "))
b=int(input("Enter The No of Seconds:  "))
c=[]
e=0
for i in range(0,a):
    d=input("Enter The Data in Capital Format: ")
    c.append(d)
for j in range(0,b):
    for i in c:
     if c[e]=="B" and c[e+1]=="G":
        c[e]="G"
        c[e+1]="B"

        e=e+1


     else:

        pass
     e=e+1
     if (e+1)>=a:
        break
    e=0
print(c)