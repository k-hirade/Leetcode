class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            # 現在の要素が候補と同じ場合はカウンターを1増やし、異なる場合は1減らす
            count += (1 if num == candidate else -1)

        return candidate
