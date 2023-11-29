class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_array = {}
        for i, num in enumerate(nums):
            if num in num_array and i - num_array[num] <= k:
                return True
            num_array[num] = i
        return False
