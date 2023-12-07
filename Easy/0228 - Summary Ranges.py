class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            # If the current number is not consecutive
            if nums[i] != nums[i - 1] + 1:
                # End of the current range
                end = nums[i - 1]
                ranges.append(f"{start}->{end}" if start != end else str(start))
                start = nums[i]

        # Add the last range
        end = nums[-1]
        ranges.append(f"{start}->{end}" if start != end else str(start))

        return ranges
