n=int(input("enter the patter number:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
for k in range(n,1,-1):
    for l in range(k-1):
        print("*",end=" ")
    print("\n")