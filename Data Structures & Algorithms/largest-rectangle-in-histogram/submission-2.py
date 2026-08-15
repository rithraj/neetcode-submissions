class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                popped = stack.pop()
                area = popped[1] * (i - popped[0])
                if area > maxArea:
                    maxArea = area
                start = popped[0]
            stack.append((start, h))

        for item in stack:
            area = (len(heights) - item[0]) * item[1]
            if area > maxArea:
                maxArea = area

        return maxArea

        