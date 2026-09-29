class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = [num for num in nums]
        a.extend(nums)
        return a