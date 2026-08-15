class Solution:
    def rob(self, nums: List[int]) -> int:

        def helpRob(houses):
            rob1, rob2 = 0,0

            for num in houses:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(nums[0], helpRob(nums[1::]), helpRob(nums[:-1]))


        