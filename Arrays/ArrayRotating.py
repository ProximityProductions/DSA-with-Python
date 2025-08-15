array = [3, 4, 5, 1, 2]
k = int(input())
n = len(array)
k = k % n

def reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array


def Rotate(array, k):
    reverse(array, 0, n - 1)
    reverse(array, 0, k - 1)
    reverse(array, k, n - 1)
    return array


print("Rotated array is:", Rotate(array))
