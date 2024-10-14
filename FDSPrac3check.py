cricket=list(input("entre roll no.of student who play cricket : ").split())
badminton=list(input("entre roll no.of student who play badminton : ").split())
foot=list(input("entre roll no.of student who play football : ").split())


#student who play both cricket and badminton
a=list()
for i in cricket:
	for j in badminton:
		if(i==j):
			a.append(i)   #either append j
			
print("student who play both crickwt and football : ",a)


#student who play either cricket or batminton but not both
b=list()
for i in cricket:
	if i not in badminton:
		b.append(i)
print("student who play only cricket are : ",b)
c=list()
for j in badminton:
	if j not in cricket:
		c.append(j)
print("student who play only badminton are : ",c)

#student who play neither cricket nor badminton
d=list()
for k in foot:
	if((k not in cricket)and(k not in badminton)):
		d.append(k)
print("student who play neither cricket nor badminton : ",d)


#student who play cricket and foorball but not badminton
e=list()
for m in cricket:
	for n in foot:
		if(m==n):
			e.append(m)    #either use n
			
f=list()
for i in e:
	if i not in badminton:
		f.append(i)
print("student who play cricket ans foltball  : ",f)