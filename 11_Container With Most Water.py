class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] <= height[right]:
                area = height[left] * (right - left)
            else:
                area = height[right] * (right - left)
            
            if area > max_area:
                max_area = area
            
            if height[left] <= height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1

        return max_area
        
height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
result = solution.maxArea(height)
print(result)
