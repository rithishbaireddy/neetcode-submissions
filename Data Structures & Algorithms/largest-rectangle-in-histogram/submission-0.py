class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                height=heights[stack.pop()]
                if not stack:
                    width=i
                else:
                    width=i-stack[-1]-1
                area=width*height
                maxarea=max(maxarea,area)        

            stack.append(i)
        return maxarea    
        