class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for index in range(numRows):
            row = [1] * (index + 1)
            for item in range(1, index):
                row[item] = triangle[index - 1][item - 1] + triangle[index - 1][item]
            triangle.append(row)
        return triangle

numRows = 5
result = Solution().generate(numRows)
print(result)
