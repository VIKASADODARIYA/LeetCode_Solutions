class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutations = [[]]
        
        while permutations:
            current = permutations.pop(0)
            if len(current) == len(nums):
                result.append(current)
            else:
                for num in nums:
                    if num not in current:
                        new_permutation = current + [num]
                        permutations.append(new_permutation)
        
        return result

nums = [1, 2, 3]
result = Solution().permute(nums)
print(result)
