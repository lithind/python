# year=int(input("enter ending year:"))
# i=2021
# while i<=year:
#     if i%4==0:
#         if i%100==0:
#             if i%400==0:
#                 print(i)
#         print(i,end=" ")
#     i=i+1
start=int(input("enter current year:"))
end=int(input("enter ending year:"))
for i in range(start,end+1):
    if (i%4==0 and i%100!=0 or i%400==0):
        print(i,end=" ")
