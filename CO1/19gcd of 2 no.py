import math
a=int(input("input enter number1:"))
b=int(input("input enter number2:"))
gcd=math.gcd(a,b)
print(gcd)
# while True:
#     a=int(input("enter first number:"))
#     b=int(input("enter second number:"))
#     gcd=0
#     if a>b:
#         for i in range(1,b+1):
#             if b%i==0:
#                 if a%i==0:
#                     gcd=i
#         print("gcd=",gcd)
#     else:
#         for j in range(1,a+1):
#             if a%j==0:
#                 if b%j==0:
#                     gcd=j
#         print("gcd=",gcd)