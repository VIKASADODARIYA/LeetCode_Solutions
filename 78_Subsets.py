class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for item in nums:
            temp = []
            for subset in result:
                temp.append(subset + [item])
            result += temp

        return result

nums = [1, 2, 3]
result = Solution().subsets(nums)
print(result)
