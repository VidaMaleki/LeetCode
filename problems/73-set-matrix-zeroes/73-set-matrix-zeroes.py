class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        b = []
        for i in range(len(matrix)):
            for j, num in enumerate(matrix[i]):
                
                if num == 0:
                    b.append(j)
                    matrix[i] = [0 for x in matrix[i]]
                    print(matrix)
        for i in range(len(matrix)):
            for j , num in enumerate(matrix[i]):
                if j in b:
                    matrix[i][j] = 0
            
        return matrix