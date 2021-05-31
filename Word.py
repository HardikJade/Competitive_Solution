a=input("Enter The Text:  ")
b=[]
c=[]
for i in a:
    d=i
    e=d.isupper()
    if e==True:
        b.append(e)
    elif e==False:
        c.append(e)
if len(b)==len(c):
    a=a.lower()
elif len(b)>len(c):
    a=a.upper()
elif len(b)<len(c):
    a=a.lower()
print(a)
