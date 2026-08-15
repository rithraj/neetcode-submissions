class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [0] * len(nums)
        # tot = 0
        # for i in range(len(nums)):
        #     prod = 1 * nums[i]
        #     tot = prod + tot

        # for i in range(len(nums)):
        #     res[i] = tot / nums[i]


        # return res

        res = [0] * len(nums)
        for i in range(len(nums)):
            tot = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prod = 1 * nums[j]
                tot = prod * tot
            res[i] = tot

        return res


        
