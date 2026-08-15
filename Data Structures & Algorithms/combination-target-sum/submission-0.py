class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        solution = []
        def dfs(val):
            if val >= target:
                if val == target:
                    possible = sorted(solution.copy())
                    if possible not in res:
                        res.append(possible)
                return
            
            for n in nums:
                val += n
                solution.append(n)
                dfs(val)
                val -=n
                solution.pop()
        dfs(0)

        return res

        