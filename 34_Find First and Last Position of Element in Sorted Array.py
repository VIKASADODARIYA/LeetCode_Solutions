class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        length = len(nums)
        for item in range(length):
            if nums[item] == target:
                result[0] = item
                break
        for item in range(length - 1, -1, -1):
            if nums[item] == target:
                result[1] = item
                break
        return result

nums = [5,7,7,8,8,10]
target = 8
solution = Solution()
result = solution.searchRange(nums, target)
print(result)
