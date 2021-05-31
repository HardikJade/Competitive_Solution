a=input("Enter The Broze Code: ")
b=[]
c=0
d="0"
for i in a:
    b.append(i)
for i in b:
    if b[c]=="-" and b[c+1]=="-":
        d=d+"2"


        c=c+1

    elif b[c]=="-" and b[c+1]==".":
        d=d+"1"


        c=c+1

    else:

        d=d+"0"



    if (c+1)>=len(a):
        break
    c=c+1
d=d[1::]
print(d)