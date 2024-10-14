#word with longest length in string

print("word with longest length\n")
str=input("entre the string : ")
s=str.split()
print(s)
m=0
                         
for i in range(len(s)):
	if(m<len(s[i])):
		m=len(s[i])
		c=i
print("word with longest len is ",s[c])



#palindrome
print("for palindeome\n")
str1=input("entre the string : ")
s1=str1[::-1]
if(s1==str1):
	print("it is palindrome")
else:
	print("not palindrome")
	
	
	
	
#occuarnce in string
print("occuarnce of the char in string\n")
str2=input("entre  the string  : \n")
s2=input("entrw the character  : ")
count=0
for i in range (len(str2)):
	if (s2==str2[i]):
		count+=1
print(s2,"occurs in string ",count,"times")


#substring in main string
print("substring is found in main string\n")
str3=input("entrw the string : \n")
sub=input("entrw the substring : ")
found=0
for i in range (len(str3)) :
	if (str3[i:i+len(sub)]==sub):
		found=1
		break;            
if(found==1):
	print("string found at ",i)
else:
	print("not found")
	
	
#occuarnce of each words
print("find occurance of each word in main string\n")
str4=input("entre the string : ")
cout=dict()
words=str4.split()
for word in words:
	if (word in cout):
		cout[word]+=1
	else:                
		cout[word]=1
print(cout)

'''i=0
while i < len(words):
	count=0
	for j in words:
		if words[i]==j:
			count=count+1
	print(words[i],count)
	i=i+1
'''