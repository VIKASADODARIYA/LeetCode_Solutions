class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        single_element = nums[0]
        for item in nums[1:]:
            if item == single_element:
                count += 1
            else:
                count -= 1
                if count == 0:
                    single_element = item
                    count = 1
        return single_element

nums = [3,2,3]
result = Solution().majorityElement(nums)
print(result)
