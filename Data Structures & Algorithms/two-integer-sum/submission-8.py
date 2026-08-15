class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for i, num in enumerate(nums):
            remainder[num] = i
        
        for i in range(len(nums)):
            r = target - nums[i]
            if r in remainder and remainder[r] != i:
                return [i, remainder[r]]
        
        return []

        