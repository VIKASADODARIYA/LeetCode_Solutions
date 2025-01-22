class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        list2 = [nums[i], nums[j], nums[k]]
                        if list2 not in result:
                            result.append([nums[i], nums[j], nums[k]])
        return result
        
nums = [-1,0,1,2,-1,-4]
solution = Solution()
result = solution.threeSum(nums)
print(result)
