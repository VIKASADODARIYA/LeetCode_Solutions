class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [n for n in nums if n > 0]
        nums.sort()
        target = 1
        for item in range(len(nums)):
            if nums[item] == target:
                target += 1
            elif nums[item] > target:
                return target
        return target

nums = [1,2,0]
result = Solution().firstMissingPositive(nums)
print(result)
