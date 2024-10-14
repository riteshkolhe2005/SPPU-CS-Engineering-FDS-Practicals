#palindrome
str1=input("enter the string\n")
co=str1[::-1]
if co==str1 :
    print("string is palindrome")
else:
    print("string is not palindrome")

#occurance of char in string
str2=input("enter string\n")
subchar=input("enter character\n")
count=0
for i in range (len(str2)):
    if str2[i]==subchar:
        count=count+1
print(subchar," occur ",count," times")

#occuarmnce of substring
str3=input("enter string\n")
substr=input("enter substring\n")
found=0
ss=0
for i in range (len(str3)):
    if (str3[i:i+len(substr)]==substr):
        found=1
        ss=i
        break;
if(found==1):
    print("string found at ",ss)
else:
    print("string is not found")

#longest word from string
str4=input("Enter string\n")
cat=str4.split()
count2=0
c1=0
for i in range (len(cat)):
    if count2 < len(cat[i]):
        count2 = len(cat[i])
        c1=i
print(cat[c1]," is the longest word")

#occurance of each word in string
str5=input("enter string\n")
cat2=str5.split()
cc=dict()

for i in cat2:
    if i in cc:
        cc[i]+=1
    else:
        cc[i]=1
print(cc)