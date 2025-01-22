class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        middleIndex = length / 2
        if length % 2 == 0:
            median = (nums1[int(middleIndex) - 1] + nums1[int(middleIndex)]) / 2
            return median
        else:
            return nums1[int(middleIndex)]
        # median = statistics.median(nums1)
        # return median
nums1 = [1,3]
nums2 = [2,4]
solution = Solution()
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)
