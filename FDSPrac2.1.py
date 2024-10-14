
                                #STRING OPERATIONS

#1=LONGEST LENGTH LONGEST 

str1=input("enter a string:")
list1=str1.split()
m=0
word=0
print(list1)
for i in range(len(list1)):
        if(m<len(list1[i])):
                m=len(list1[i])
                word=i
print(len(list1[word]))


#2=occurance of character

char=input("Enter character: ")
counter=0
for i in range(len(str1)):
        if(char==str1[i]):
                counter=counter+1
                
print("no of char in string :",counter)            


#3=palindrom string
  
str2=str1[::-1]
if(str1==str2):
        print("string is palindrom")
else:
        print("string is not palindrom")
        
        


#4=finding sub string
                
sub=input("enter a sub string:")
for i in range(len(str1)):
        if(str1[i:i+len(sub)]==sub):
                found=1
                break
        #else:
                #print("substring is not found")
if(found==1):
        print("sub string found at:",i) 
       
else:
        print("no substring")



#5=occurance of each word
        
count=dict()
words=str1.split()  

for w in words:
        if(w in count):
                count[w]+=1
        else:
                count[w]=1 
print(count)            
        
        
              
        
