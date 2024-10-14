a=int(input("enter the total no. of student : "))
A=[]
for i in range(a):
    r=float(input("enter the first year percentage of student : "))
    A.append(r)
print("the list of percentage of student : ",A)

#bubble sort
def bubble():
    j=0
    for k in range(a-1):
        s=0
        for i in range(a-1):
            j=i+1
            if(A[i]>A[j]):
                A[i],A[j]=A[j],A[i]
                s=s+1
        print(A)
        if(s==0):
            break
    print("the sorted list of percentage : ",A)
bubble()

#selection sort
def selection():
    for i in range(a-1):
        mini=i
        for j in range(i+1,a):
            if(A[j]<A[mini]):
                mini=j
        if(mini!=i):
            A[i],A[mini]=A[mini],A[i]  
    print("the sorted list of percentage : ",A)
selection()