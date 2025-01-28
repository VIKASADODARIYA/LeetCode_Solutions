class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # for index in range(len(nums) - 1):
        #     for index2 in range(index + 1, len(nums)):
        #         if nums[index] < nums[index2]:
        #             temp = nums[index]
        #             nums[index] = nums[index2]
        #             nums[index2] = temp

        nums.sort(reverse = True)
        
        return nums[k - 1]

nums = [3, 2, 1, 5, 6, 4]
k = 2
result = Solution().findKthLargest(nums, k)
print(result)
