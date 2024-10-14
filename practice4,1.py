n=int(input("enter total no. of students :"))
A=[]
for i in range(n):
    a1=int(input("enter roll no :"))
    A.append(a1)

print(A)

#linear search
'''key=int(input("Enter no. you want to search :"))
for i in range(n):
    if A[i]==key:
        print("found at ",i)
    

#sentinel search
key2=int(input("enter no. you want to search :"))
last=A[n-1]
A[n-1]=key2
i=0
while A[i]!=key2:
    i+=1
A[n-1]=last

if (i< n-1)or(A[n-1]==key):
    print("found at ",i)
else:
    print("not found")'''

#binary search

'''def binarysearch(A,n,key3):
    start=0
    end=n-1
    while start <= end:
        mid=(start+end)//2

        if key3==A[mid]:
            return mid
        elif key3 > A[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1

key3=int(input("Enter number you want to search"))
res=binarysearch(A,n,key3)
if res == -1:
    print("not found")
else:
    print("found at ",res)'''

#fibsearch
def fibsearch(A,n,key4):
    offset=-1
    f0=0
    f1=1
    f2=1
    while f2 < n:
        f0=f1
        f1=f2
        f2=f1+f0

    while f2 > 1:
        index=min(offset+f0,n-1)
        if A[index] > key4:
            f2=f0
            f1=f1-f0
            f0=f2-f1
        elif A[index] < key4:
            f2=f1
            f1=f0
            f0=f2-f1
            offset=index
        else:
            return index
        
    if f1 and A[n-1]==key4:
        return n-1
    return -1


key4=int(input("enter the no for fibsearch you want to search :"))
res1=fibsearch(A,n,key4)
if res1 == -1:
    print("not found")
else:
    print("found at ",res1)
