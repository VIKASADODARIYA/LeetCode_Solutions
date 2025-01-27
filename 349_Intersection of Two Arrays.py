class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        result = set1 & set2
        return list(result)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = Solution().intersection(nums1, nums2)
print(result)
