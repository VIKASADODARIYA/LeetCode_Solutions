class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_number = None
        multi_num = []
        
        for item in range(len(nums)):
            frequency = nums.count(nums[item])
            if frequency >= 3:
                multi_num.append(nums[item])
            else:
                return nums[item]
nums = [2,2,3,2]
result = Solution().singleNumber(nums)
print(result)
