class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # BRUTE FORCE
        # res = []
        # solution = []
        # def dfs(val):
        #     if val >= target:
        #         if val == target:
        #             possible = sorted(solution.copy())
        #             if possible not in res:
        #                 res.append(possible)
        #         return
            
        #     for n in nums:
        #         val += n
        #         solution.append(n)
        #         dfs(val)
        #         val -=n
        #         solution.pop()
        # dfs(0)

        # return res
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        
        dfs(0, [], 0)
        return res

        