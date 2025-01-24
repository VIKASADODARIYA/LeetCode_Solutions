class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = 0
        for item in nums:
            if jump < 0:
                return False
            elif item > jump:
                jump = item
            jump -= 1
        return True

nums = [2,3,1,1,4]
result = Solution().canJump(nums)
print(result)
