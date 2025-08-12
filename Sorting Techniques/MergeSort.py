def merge(left, right):
    merged = []
    i = j = 0

    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def mergeSort(array):
    # Base case: if the array is of length 0 or 1, it is already sorted
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = mergeSort(array[:mid])
    right_half = mergeSort(array[mid:])
    
    return merge(left_half, right_half)


# Input and output
array = list(map(int, input("Enter the elements of the array separated by space: ").split()))
sorted_array = mergeSort(array)
print("Sorted array:", sorted_array)
