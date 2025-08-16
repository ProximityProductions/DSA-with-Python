array = [10, 5, 2, 7, 1, 4]
k = int(input("Enter the value of k: "))


def LongestSubarrayWithKSum(array, k):
    cum_sum = 0
    max_length = 0
    max_sum_dict = {}
    for i in range(len(array)):
        cum_sum += array[i]
        if cum_sum == k:
            max_length = i + 1
        if cum_sum - k in max_sum_dict:
            max_length = max(max_length, i - (max_sum_dict[cum_sum - k]))
        if cum_sum not in max_sum_dict:
            max_sum_dict[cum_sum] = i
    return max_length
