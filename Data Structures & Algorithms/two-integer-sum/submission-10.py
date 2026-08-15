class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}
        for i in range(len(nums)):
            indicies[nums[i]] = i
        
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in indicies and indicies[remainder] != i:
                return [i, indicies[remainder]]
        