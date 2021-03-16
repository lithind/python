# (a) Generate positive list of numbers from a given list of integers
lis1=[2,-1,0,-9,5,8,1,-11]
lis2=[x for x in lis1 if x>0]
print(lis2)
# (b) Square of N numbers
l1=[]
element=int(input("enter the number of element:"))
for i in range(element):
    ele=int(input("enter element:"))
    l1.append(ele)
print(l1)
Square=[x**2 for x in l1]
print("square of list elements:",Square)
# (c) Form a list of vowels selected from a given word
n=input("enter the word:")
result=[x for x in n if x in ['a','e','i','o','u']]
print(result)
# (d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)
word=input("enter the word:")
ordvalue=[ord(i) for i in word]
print(ordvalue)
