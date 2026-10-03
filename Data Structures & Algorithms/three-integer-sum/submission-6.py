class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur == 0:
                    seen.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif cur < 0:
                    l += 1
                elif cur > 0:
                    r -= 1

        return list(seen)