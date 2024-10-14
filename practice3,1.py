cricket=list(input("enter number for cricket :").split())
badminton=list(input("enter for badminton :").split())
football=list(input("enter for football :").split())

#students who play both cricket and badminton
a=list()
for i in cricket:
    for j in badminton:
        if i==j:
            a.append(i)
print("students who play cricket and badminton are :",a)

#students who play either cricket or badminton but not both
b=list()
for i in cricket:
    if i not in badminton:
        b.append(i)

for j in badminton:
    if j not in cricket:
        b.append(j)

print("students who play either cricket or badminton but not both :",b)

#students who play neither cricket nor badminton
c=list()
for i in football:
    if (i not in cricket)and(i not in badminton):
        c.append(i)

print("students who play neitehr cricket nor badminton :",c)

#students who play cricekt and football but not badminton
d=list()
for i in cricket:
    for j in football:
        if i==j:
            d.append(i)
e=list()
for i in d:
    if i not in badminton:
        e.append(i)

print("students who play cricket and football but not badminton :",e)


