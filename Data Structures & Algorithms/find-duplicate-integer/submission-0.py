class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            print(num)
            idx = abs(num) - 1
            if nums[idx] < 0:
                print(nums)
                return abs(num)
            nums[idx] *= -1
            print(nums[idx])
        print(nums)
        return -1
        