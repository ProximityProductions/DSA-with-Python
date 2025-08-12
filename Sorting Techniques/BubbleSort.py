array = list(map(int, input("Enter the elements of the array separated by space: ").split()))

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                # Swap if the element found is greater than the next element
                array[j], array[j+1] = array[j+1], array[j]
    return array


sorted_array = bubble_sort(array)
print("Sorted array:", sorted_array)
                
