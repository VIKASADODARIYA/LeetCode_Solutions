class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for index in range(len(nums) - 1):
            for item in range(len(nums) - index - 1):
                if nums[item] > nums[item+1]:
                    temp = nums[item]
                    nums[item] = nums[item+1]
                    nums[item+1] = temp
        return nums

nums = [2,0,2,1,1,0]
result = Solution().sortColors(nums)
print(result)
