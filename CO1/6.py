li=[]
c=0
n=int(input("enter the number of names:"))
for i in range (1,n+1):
  x=input("enter first names:")
  li.append(x)
for i in li:
  for j in i:
    if 'a' in j:
      c=c+1
print("number of a's :",c)
