class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = None
        
        for item in range(len(nums)):
            frequency = nums.count(nums[item])
            if frequency == 1:
                single_number = nums[item]
        return single_number

nums = [3,2,3]
result = Solution().singleNumber(nums)
print(result)
