class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n

        high = 0
        for i in range(1, n):
            if height[i-1] > high:
                high = height[i-1]
            left[i] = high
        
        high = 0
        for i in range(n - 2, -1, -1):
            if height[i+1] > high:
                high = height[i+1]
            right[i] = high
        
        total = 0
        for i in range(n):
            min_wall = min(left[i], right[i])
            print(min_wall - height[i])
            if height[i] < min_wall:
                total += min_wall - height[i]


        return total

        