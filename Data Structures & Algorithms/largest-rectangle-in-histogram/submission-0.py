class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxArea = 0

        for idx, height in enumerate(heights):

            if not stack:
                stack.append((height, idx))
                continue
            
            start = idx
            while stack and height < stack[-1][0]:

                h, i = stack.pop()

                maxArea = max(maxArea, h * (idx - i))
                
                start = i

            stack.append((height, start))
        
        for h, i in stack:

            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
