array1 =  [1, 2, 3, 4, 5]
array2 = [1, 2, 6, 7]

def UnionOfArray(arr1,arr2):
    i,j = 0
    last = None
    UnionArray = []
    n1 = len(arr1)
    n2 = len(arr2)
    while i<n1 and j<n2:
        if arr1[i]<=arr2[j]:
            if last!= arr1[i]:
                UnionArray.append(arr1[i])
                last = arr1[i]
            i+=1
        elif arr1[i]>arr2[j]:
            if last!= arr2[j]:
                UnionArray.append(arr2[j])
                last = arr2[j]
            j+=1
    while i<n1:
        if last!= arr1[i]:
            UnionArray.append(arr1[i])
            last = arr1[i]
        i+=1

    while j<n2:
        if last!= arr2[j]:
            UnionArray.append(arr2[j])
            last = arr2[j]
        j+=1

    return UnionArray
