class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) < 2:
            return 0

        gap = []
        for index in range(len(nums) - 1):
            gap_value = abs(nums[index] - nums[index + 1])
            gap.append(gap_value)

        gap2 = []
        for index in range(len(nums) - 1, 0, -1):
            gap_value2 = abs(nums[index] - nums[index - 1])
            gap2.append(gap_value2)
        
        gap2.reverse()
        if gap == gap2:
            return max(gap)


nums = [3,6,9,1]
Solution().maximumGap(nums)
