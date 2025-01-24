class Solution:
    def jump(self, nums: List[int]) -> int:
        max_jump = 0
        steps = 0
        jump = 0
        for item in range(len(nums)-1):
            jump = max(jump, item + nums[item])
            if item == steps:
                max_jump += 1
                steps = jump
        return max_jump

nums = [2,3,1,1,4]
result = Solution().jump(nums)
print(result)
