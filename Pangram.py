a=input("Enter The String:  ")
i=0
for j in a:
    b=a[i]
    if b in a[i+1::]:
        print("NO")
        exit()
    else:
        i=i+1
print("YES")