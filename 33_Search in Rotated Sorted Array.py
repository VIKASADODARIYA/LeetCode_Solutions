class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for index in range(len(nums)):
            if nums[index] == target:
                return index
            
        return -1

nums = [4,5,6,7,0,1,2]
target = 0
solution = Solution()
result = solution.search(nums, target)
print(result)
