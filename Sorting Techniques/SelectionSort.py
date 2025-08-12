array = list(map(int, input("Enter numbers separated by space: ").split()))


def SelectionSort(array):
    for i in range(len(array)):
        box = i
        for j in range(i + 1, len(array)):
            if array[j] < array[box]:
                box = j
        array[i], array[box] = array[box], array[i]
    return array


sorted_array = SelectionSort(array)
print("Sorted array:", sorted_array)
