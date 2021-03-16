# word=input("enter the word:")
# n=len(word)
# for i in word[0:n]:
#     if i==word[0]:
#         print("$",end="")
#     elif word[0]==word[0]:
#         print(i,end="")
#     else:
#         print(i)
word=input("enter the word:")
word1=word
frst=word[0]
word=word.replace(frst,"$")
word=frst+word[1:]
print(word1,">>",word)
