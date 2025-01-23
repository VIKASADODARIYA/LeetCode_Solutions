class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        pivot = length - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        if pivot >= 0:
            index = length - 1
            while nums[index] <= nums[pivot]:
                index -= 1
            nums[pivot], nums[index] = nums[index], nums[pivot]

        left, right = pivot + 1, length - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
nums = [1,2,3]
solution = Solution()
result = solution.nextPermutation(nums)
print(result)
