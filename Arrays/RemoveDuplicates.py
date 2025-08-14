array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

def RemoveDuplicates():
    j = 0
    for i in range(1,len(array)):
        if array[i]!=array[j]:
            j+=1
            array[j] = array[i]
    return j+1