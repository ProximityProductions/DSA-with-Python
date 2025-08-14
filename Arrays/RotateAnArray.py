def reverse(start, end, nums):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate(nums, k):
    k = k % len(nums)

    reverse(0, len(nums) - 1, nums)

    reverse(0, k - 1, nums)

    reverse(k, len(nums) - 1, nums)


nums = list(
    map(int, input("Enter the elements of the array separated by spaces: ").split())
)
k = int(input("Enter the number of rotations: "))

rotate(nums, k)
print("Rotated array:", nums)
