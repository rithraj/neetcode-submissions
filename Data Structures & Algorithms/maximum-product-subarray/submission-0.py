class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = max(nums)

        for num in nums:
            tmp = currMax * num
            currMax = max(num, num * currMax, num * currMin)
            currMin = min(num, num * currMin, tmp)
            res = max(res, currMax)

        return res



        