class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1

        result = 0

        while left < right: 
            # area of rectangle is L x W 
            width = right - left # reminder this is index not value of height[right] and height[left]
            height = min(heights[left], heights[right]) # we want to get the min height because it would overflow 
            area = width * height 
            result = max(result, area) # keep track of the maximum area 

            if heights[left] < heights[right]: # we want to move the pointer with smallest height
                left+=1
            else:
                right-=1

        return result