class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [1] * n

        # Pass 1: fill ret[i] with product of everything to the LEFT of i
        prefix = 1
        for i in range(n):
            ret[i] = prefix
            prefix *= nums[i]

        print(f"prefix : {ret}")

        # Pass 2: multiply in the product of everything to the RIGHT of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            ret[i] *= suffix
            suffix *= nums[i]
        print(f"suffix : {ret}")

        return ret