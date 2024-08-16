class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            width = right - left
            heightLeft = height[left]
            heightRight = height[right]

            currentArea = min(heightLeft, heightRight) * width
            maxArea = max(maxArea, currentArea)

            if heightLeft <heightRight:
                left +=1
            else:
                right-= 1

        return maxArea
