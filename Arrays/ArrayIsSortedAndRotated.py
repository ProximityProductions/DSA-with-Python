array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

def isarraysorted(array):
    count = 0
    n = len(array)
    for i in range(n):
        if array[i] > array[(i + 1) % n]:  # wrap around using modulo
            count += 1
    return count <= 1

isarraysorted_result = isarraysorted(array)
print("Is the array sorted in non-decreasing order (possibly rotated)? :", isarraysorted_result)
