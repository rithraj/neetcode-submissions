class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_dict = {}
        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = n + 1
        longest = []
        for n in nums:
            res = []
            cond = True
            x = n
            while cond:
                if nums_dict[x] in nums:
                    res.append(x)
                else:
                    res.append(x)
                    cond = False

                x = nums_dict[x]

            if len(res) > len(longest):
                longest = res
            
        return len(longest)

                    

        