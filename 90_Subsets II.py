class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        result.add(())
        
        for item in nums:
            temp = set()
            for subset in result:
                temp.add(tuple(list(subset) + [item]))
            result.update(temp)
        
        return list(result)

nums = [1, 2, 2]
result = Solution().subsetsWithDup(nums)
print(result)
