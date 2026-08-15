class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l, r = 0, len(heights) - 1
        while l < r:
            volume = min(heights[l], heights[r]) * (r - l)
            if volume > largest:
                largest = volume
            if heights[l] > heights[r]:
                r = r-1
            else:
                l = l + 1
        return largest




        