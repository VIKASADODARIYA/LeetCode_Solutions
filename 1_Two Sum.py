class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        # num={}
        # for i in range(len(nums)):
        #     r = target - nums[i]
        #     if r in num:
        #         return [num[r],i]
        #     num[nums[i]]=i
        # return []


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)
