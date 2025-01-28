class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        previous, current = 0, 0
        for num in nums:
            temp = max(previous, current + num)
            current = previous
            previous = temp
        
        return previous

nums = [1, 2, 3, 1]
result = Solution().rob(nums)
print(result)
