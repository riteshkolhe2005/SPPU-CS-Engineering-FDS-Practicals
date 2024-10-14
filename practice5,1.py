n=int(input("enter total no. of students :"))
A=[]
for i in range(n):
    a1=int(input("enter roll no :"))
    A.append(a1)

print(A)

#bubble sort
for i in range(0,n-1):

    for j in range(0,n-1):
        
        if A[j] > A[ j + 1] :
            temp=A[j]
            A[j]=A[j+1]
            A[j+1]=temp
print(A)

#selection sort
for i in range(n):
    mini=i
    for j in range(i+1,n):
        if A[j] < A[mini]:
            mini=j

    temp=A[i]
    A[i]=A[mini]
    A[mini]=temp

print(A) 

#quick sort
def partition(A,low,high):
    pivot=A[low]
    i=low+1
    j=high

    while True:
        while i <= j and A[i] <= pivot:
            i+=1
        while i <= j and A[j] >= pivot:
            j-=1

        if i <= j:
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
        else:
            break;
    temp1=A[low] 
    A[low]=A[j]
    A[j]=temp1

    return j

def quicksort(A,low,high):
    if low < high:
        pivot1=partition(A,low,high)
        quicksort(A,low,pivot1-1)
        quicksort(A,pivot1+1,high)

quicksort(A,0,n-1)
print(A)



