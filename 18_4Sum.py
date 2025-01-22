class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        length = len(nums)
        if length < 4:
            return []
        for i in range(length):
            for j in range(i+1, length):
                k = j + 1
                l = length - 1
                while k < l:                    
                        sum = nums[i] + nums[j] + nums[k] + nums[l]
                        if sum == target:
                            result.add((nums[i], nums[j], nums[k], nums[l]))
                            k += 1
                        if sum < target:
                            k += 1
                        else:
                            l -= 1
        return list(result)

nums = [1,0,-1,0,-2,2]
target = 0
solution = Solution()
result = solution.fourSum(nums, target)
print(result)
