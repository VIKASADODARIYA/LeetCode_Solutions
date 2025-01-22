# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         result = []
#         length = len(nums)
#         for i in range(length):
#             for j in range(i+1, length):
#                 for k in range(j+1, length):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         list2 = [nums[i], nums[j], nums[k]]
#                         if list2 not in result:
#                             result.append([nums[i], nums[j], nums[k]])
#         return result
        
# nums = [-1,0,1,2,-1,-4]
# solution = Solution()
# result = solution.threeSum(nums)
# print(result)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)
        
        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, length - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
result = solution.threeSum(nums)
print(result)
