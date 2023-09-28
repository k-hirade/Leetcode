def twoSum(nums, target):
    num_index = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in num_index:
            return [num_index[diff], i]
        num_index[num] = i

# In this solution, we iterate through the nums array and at each iteration, we calculate the difference between the target and the current number. We check if this difference is in the num_index dictionary. If it is, we have found two numbers whose sum is equal to the target, and we return their indices. If not, we add the current number and its index to the num_index dictionary.
