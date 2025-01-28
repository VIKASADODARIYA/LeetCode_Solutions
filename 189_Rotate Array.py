class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k > 0:
            temp = nums.pop()
            nums.insert(0,temp)
            k -= 1
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
result = Solution().rotate(nums, k)
print(result)
