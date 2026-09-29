class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        pairs = []
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                pairs.extend([seen[complement], i])
            seen[num] = i
        return pairs

        