n=int(input("enter the total no. of student : "))
A=[]
for i in range(n):
    r=float(input("enter the first year percentage of student : "))
    A.append(r)
print("the list of percentage of student : ",A)

def partition(A,start,end):
    pindex=start
    pivot=end
    for i in range(start,end):
        if(A[pivot]>A[i]):
            A[i],A[pindex]=A[pindex],A[i]
            pindex=pindex+1
    A[pivot],A[pindex]=A[pindex],A[pivot]
    print(A)
    return pindex
def QS(A,start,end):
    if start<end:
        pindex=partition(A,start,end)
        QS(A,start,pindex-1)
        QS(A,pindex+1,end)
QS(A,0,n-1)
