array = list(map(int, input("Enter the elements of the array separated by space: ").split()))

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

sorted_array = insertion_sort(array)
print("Sorted array:", sorted_array)
