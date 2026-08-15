class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        res = []
        q = deque()
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
        
            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
        
        # l = 1, r = k
        # q.append(nums[0])
        # for i in range(1,k):
        #     if nums[-1] < nums[i]:
        #         q.pop()
        #         q.append(i)
        
        # while r < len(nums):
        #     while q and nums[q[-1]] < nums[r]:
        #         q.pop()
        #     q.append(r)

        #     if l > q[0]:
        #         q.popleft()
            
            # if r + 1 >= k

            
        