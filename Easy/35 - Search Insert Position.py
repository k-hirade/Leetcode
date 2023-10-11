# 80ms
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return_value = 0
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if target >= nums[i]:
                    return_value = i+1
            return return_value

# 71ms
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if nums[i] >= target:
#                 return i
#         return len(nums)
