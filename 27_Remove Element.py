class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        value = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[value] = nums[index]
                value += 1
        return value

nums = [3,2,2,3]
value = 3
solution = Solution()
result = solution.removeElement(nums, value)
print(result)
