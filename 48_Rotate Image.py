class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for row in range(len(matrix)):
            for column in range(row):
                temp = matrix[row][column]
                matrix[row][column] = matrix[column][row]
                matrix[column][row] = temp
        return matrix
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = Solution().rotate(matrix)
print(result)
