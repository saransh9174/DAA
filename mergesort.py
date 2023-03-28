def mergesort(arr):
    if len(arr)>1:
        r=len(arr)//2
        l=arr[:r]
        m=arr[r:]

        mergesort(l)
        mergesort(m)
        i=j=k=0

        while i<len(l) and j<len(m):
            if l[i]<m[j]:
                arr[k]=l[i]
                i+=1
                
            else:
                arr[k]=m[j]
                j+=1
                k+=1
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(m):
            arr[k]<m[j]
            j+=1
            k+=1

def printlist(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()
    
arr=[6,5,12,10,9,1]
mergesort(arr)
print("sorted arr: ")
printlist(arr)
# T(n) = 2T(n/2) + O(n) The solution of the above recurrence is O(nLogn).