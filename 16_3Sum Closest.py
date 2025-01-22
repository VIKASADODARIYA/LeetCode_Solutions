class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length = len(nums)
        result = nums[0] + nums[1] + nums[2]
        for index in range(length - 2):
            left = index + 1
            right = length - 1
            while left < right:
                sum = nums[index] + nums[left] + nums[right]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
        return result

nums = [-1,2,1,-4]
target = 1
solution = Solution()
result = solution.threeSumClosest(nums, target)
print(result)
