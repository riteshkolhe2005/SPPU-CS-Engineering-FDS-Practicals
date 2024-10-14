t=int(input("the total strength of class : "))
T=[]
for i in range(t):
    T.append(i+1)
print("roll no of all student",T)
key=int(input("the roll no. you want to check : "))

#code fo linear search
def lsearch():
    for i in range(t):
        if(key==T[i]):
            print("student is present")
            break
    else:
        print("student is absent")
lsearch()

#code for sentinal search 
last = arr[n - 1]
 
    # Element to be searched is
    # placed at the last index
    arr[n - 1] = key
    i = 0
 
    while (arr[i] != key):
        i += 1
 
    # Put the last element back
    arr[n - 1] = last
 
    if ((i < n - 1) or (arr[n - 1] == key)):
        print(key, "is present at index", i)
    else:
        print("Element Not found")
 

#code for binary search 
def bsearch():
    while l <= r:
 
        mid = l + (r - l) // 2
 
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
 
    # If we reach here, then the element
    # was not present
    return -1
 
 
# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
 
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")

#code for fibonacci search
def fsearch():
    f1=1
    f2=0
    f=f1+f2
    while(f<t):
        f1=f
        f2=f1
        f=f1+f2
    i=0
    offset=-1
    while(f>1):
        i=min(offset+f2,t-1)
        if(T[i]==key):
            print("the student is present")
            break
        if(key>T[i]):
            f=f1
            f1=f2
            f2=f-f1
            offset=i
        if(key<T[i]):
            f=f2
            f1=f1-f2
            f2=f-f1
    else:
        print("the student is absent")
fsearch()


#fibsearch
def fibonacci_search(lst, target):
    size = len(lst)
    
    offset = -1
    
    f0 = 0
    f1 = 1
    f2 = 1
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    
    
    while(f2 > 1):
        index = min(offset + f0, size - 1)
        if lst[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            offset = index
        elif lst[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (lst[size - 1] == target):
        return size - 1
    return -1


    #fib option
    # Initialize fibonacci numbers 
    fibMMm2 = 0  # (m-2)'th Fibonacci No. 
    fibMMm1 = 1  # (m-1)'th Fibonacci No. 
    fibM = fibMMm2 + fibMMm1  # m'th Fibonacci 
  
    # fibM is going to store the smallest 
    # Fibonacci Number greater than or equal to n 
    while (fibM < n): 
        fibMMm2 = fibMMm1 
        fibMMm1 = fibM 
        fibM = fibMMm2 + fibMMm1 
  
    # Marks the eliminated range from front 
    offset = -1
  
    # while there are elements to be inspected. 
    # Note that we compare arr[fibMm2] with x. 
    # When fibM becomes 1, fibMm2 becomes 0 
    while (fibM > 1): 
  
        # Check if fibMm2 is a valid location 
        i = min(offset+fibMMm2, n-1) 
  
        # If x is greater than the value at 
        # index fibMm2, cut the subarray array 
        # from offset to i 
        if (arr[i] < x): 
            fibM = fibMMm1 
            fibMMm1 = fibMMm2 
            fibMMm2 = fibM - fibMMm1 
            offset = i 
  
        # If x is less than the value at 
        # index fibMm2, cut the subarray 
        # after i+1 
        elif (arr[i] > x): 
            fibM = fibMMm2 
            fibMMm1 = fibMMm1 - fibMMm2 
            fibMMm2 = fibM - fibMMm1 
  
        # element found. return index 
        else: 
            return i 
  
    # comparing the last element with x */ 
    if(fibMMm1 and arr[n-1] == x): 
        return n-1
  
    # element not found. return -1 
    return -1
  
  
# Driver Code 
arr = [10, 22, 35, 40, 45, 50, 
       80, 82, 85, 90, 100,235] 
n = len(arr) 
x = 235
ind = fibMonaccianSearch(arr, x, n) 
if ind>=0: 
  print("Found at index:",ind) 
else: 
  print(x,"isn't present in the array"); 