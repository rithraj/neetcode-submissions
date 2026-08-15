class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Solution here is not to splice but instead to iterate around the corners and we will be system
        l, r = 0, len(nums) - 1
        if len(nums) == 1 and target == nums[0]:
            return 0

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m -1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
