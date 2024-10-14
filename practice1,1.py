r1 = int(input("enter the rows for matrix A\n"))
c1 = int(input("enter column for matrix A\n"))
r2 = int(input("enter the rows for matrix B\n"))
c2 = int(input("enter column for matrix B\n"))

A = []
for i in range(r1):
    a = []
    for j in range(c1):
        a.append(int(input(f"Enter A[{i}][{j}]")))
    A.append(a)

for i in A:
    print(i)

B = []
for i in range(r2):
    b = []
    for j in range(c2):
        b.append(int(input(f"Enter B[{i}][{j}]")))
    B.append(b)

for i in B:
    print(i)

c=int(input("enter choice :\n1.Add\n2.sub\n3.mul\n4.transpose A\n5.transpose B\n"))
match c:
    case 1:
        if((r1==r2)and(c1==c2)):
            sum=[]
            for i in range(r1):
                s=[]
                for j in range(r2):
                    val=A[i][j]+B[i][j]
                    s.append(val)
                sum.append(s)
        
            for i in sum:
                print(i)
        else:
            print("Add not possible")

    case 2:
        if((r1==r2)and(c1==c2)):
            sub=[]
            for i in range(r1):
                s1=[]
                for j in range(r2):
                    val1=A[i][j]-B[i][j]
                    s1.append(val1)
                sub.append(s1)
        
            for i in sub:
                print(i)
        else:
            print("sub not possible")

    case 3:
        if(c1==r2):
            mul=[]
            for i in range(r1):
                m=[]
                for j in range(c2):
                    m.append(0)                      
                mul.append(m)
            

            for i in range(r1):
                for j in range(c2):
                    for k in range(r2):
                        mul[i][j]+=A[i][k]*B[k][j]

            for i in mul:
                print(i)
        else:
            print("mul not possible")

    case 4:
        trans1=[]
        for i in range(c1):
            t1=[]
            for j in range(r1):
                t1.append(0)
            trans1.append(t1)

        for i in range(r1):
            for j in range(c1):
                trans1[j][i]=A[i][j]

        for i in trans1:
            print(i)

    case 5:
        trans2=[]
        for i in range(c2):
            t2=[]
            for j in range(r2):
                t2.append(0)
            trans2.append(t2)

        for i in range(r2):
            for j in range(c2):
                trans2[j][i]=B[i][j]

        for i in trans2:
            print(i)

