def moveZeroes(nums):
        j = 0 
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return nums

nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
moveZeroes(None, nums)
print("Array after moving zeroes:", nums)
