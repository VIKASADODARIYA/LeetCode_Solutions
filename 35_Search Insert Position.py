class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        for index in range(length):
            if nums[index] == target:
                return index
            else:
                nums.append(target) #[1,3,5,6,2]
                nums.sort() #[1,2,3,5,6]
                return nums.index(target)

nums = [1,3,5,6]
target = 2
solution = Solution()
result = solution.searchInsert(nums, target)
print(result)
