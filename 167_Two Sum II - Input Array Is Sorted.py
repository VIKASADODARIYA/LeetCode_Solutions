class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

numbers = [2, 3, 4]
target = 6
result = Solution().twoSum(numbers, target)
print(result)
