r=int(input("enter the number of rows of first matrix : "))
c=int(input("enter the number of colunm of first matrix : "))

M1=[]
M2=[]
# Taking the element of first matrix
for i in range(r):
    sub=[]
    for j in range(c):
        u=int(input("enter the element of :"))
        sub.append(u)
    M1.append(sub)

r2=int(input("enter the number of rows of second matrix : "))
c2=int(input("enter the number of colunm of second matrix : "))
# Taking the element of second matrix
for i in range(r2):
    b=[]
    for j in range(c2):
        u=int(input("enter the element of :"))
        b.append(u)
    M2.append(b)
    
#addition of two matrix
def addition():
    add=[]
    if(r==r2 and c==c2):
        for i in range(r):
            s=[]
            for j in range(c):
                a=M1[i][j]+M2[i][j]
                s.append(a)
            add.append(s)
        print("addition of matrix is : \n",add)
        for i in add:
            print(i)
    else:
        print("addition can't be perform")
def substraction():
    sub=[]
    if(r==r2 and c==c2):
        for i in range(r):
            s=[]
            for j in range(c):
                a=M1[i][j]-M2[i][j]
                s.append(a)
            sub.append(s)
        print("substraction of matrics is : \n",sub)
        for j in sub:
            print(j)
    else:
        print("substraction can't be perform") 
        
#matrix multiplication 
def  multiplication():
    if(c==r2):
        multi=[]
        for i in range(r):
            s=[]
            for j in range(c2):
                s.append(0)
            multi.append(s)
        for i in range(r):
            for j in range(c2):
                for k in range(r2):
                    multi[i][j]+=M1[i][k]*M2[k][j]
        print("multiplication of matrics is : \n",multi)
        for i in multi:
            print(i)
    else:
        print("multiplication can not be perform")

#transpose of matrix
def transpose():
    tran=[]
    for i in range(c):
        s=[]
        for j in range(r):
            s.append(0)
        tran.append(s)
    for i in range(r):
        for j in range(c):
            tran[j][i]=M1[i][j]
    print("transpose of matrix is \n",tran)
    for i in tran:
        print(i)
addition()
substraction()
multiplication()
transpose()
