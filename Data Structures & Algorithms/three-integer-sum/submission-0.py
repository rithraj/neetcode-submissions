class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums) - 2):
            for j in range(1, len(nums) - 1):
                for k in range(2, len(nums)):
                    if (i != j and j != k and i != k) and nums[i] + nums[j] + nums[k] == 0:
                        app = sorted([nums[i], nums[j], nums[k]])
                        if app not in res:
                            res.append(app)
        
        return res

        