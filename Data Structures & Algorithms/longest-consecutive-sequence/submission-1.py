class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        res = 0
        for n in nums:
            hashset.add(n)
        
        for num in hashset:
            if num - 1 not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1
                res = max(res, length)

        return res