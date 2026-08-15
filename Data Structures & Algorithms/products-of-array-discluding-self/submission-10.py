class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Easiest solution is to do this:
        # multiply them all out get the total product and then divide
        # by the nums[i] val

        # ret = []
        # prod = 1
        # for num in nums:
        #     if num != 0:
        #         prod = prod * num
        
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         ret.append(int(prod/nums[i]))
        #     else:
        #         ret.append(int(prod))
        
        # return ret

        ret = []
        for i in range(len(nums)):
            prod = 1
            for x in range(0, i):

                prod = prod * nums[x]

            for y in range(i+1, len(nums)):
                prod = prod * nums[y]
            ret.append(prod)
        return ret
