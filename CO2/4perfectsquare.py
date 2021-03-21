import math
for i in range(1,100):
    flag = 1
    num=i
    while num>0 :
        digit = num%10
        if digit not in [0,2,4,6,8]:
            flag=0
            break
        num=num//10
    if flag==1 and math.sqrt(i)%1==0:
        print(i)
