array = [1,4,3,7,9,2]
def LargestValue(array):
    Largest = array[0]

    for i in range(1,len(array)):
        if array[i]> Largest:
            Largest = array[i]
    return Largest

print(LargestValue(array))
