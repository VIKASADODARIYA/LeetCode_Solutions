class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        if target in nums:
            return True
        else:
            return False

nums = [2,5,6,0,0,1,2]
target = 0
result = Solution().search(nums, target)
print(result)
