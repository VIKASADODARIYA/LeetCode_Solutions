class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        index = 2

        for item in range(2, len(nums)):
            if nums[item] != nums[index-2]:
                nums[index] = nums[item]
                index += 1
        return index

nums = [1,1,1,2,2,3]
result = Solution().removeDuplicates(nums)
print(result)
