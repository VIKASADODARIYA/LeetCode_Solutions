class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(0, len(nums) - 1 - i):
                if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        result = list(map(str, nums))
        final_result = ''.join(result)
        if nums[0] == 0:
            return "0"
        return final_result

nums = [10, 2]
result = Solution().largestNumber(nums)
print(result)
