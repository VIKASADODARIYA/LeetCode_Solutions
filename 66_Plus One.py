class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []

        list_str = int(''.join(map(str, digits))) + 1
        str_list = map(int, str(list_str))

        return list(str_list)

digits = [1,2,3]
result = Solution().plusOne(digits)
print(result)
