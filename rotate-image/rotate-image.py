class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
                 [[7,4,1],[8,5,2],[9,6,3]]
                 
                 matrix[0]=> matrix[0][0], matrix[1][0], matrix[2][0]
                 matrix[1]=> matrix[0][1], matrix[1][1], matrix[2][1]
                 matrix[2]=> matrix[0][2], matrix[1][2], matrix[2][2]
                 
                 0      1.      2 
                 012    012    012
                 matrix[0]=> matrix[2][0], matrix[1][0], matrix[0][0]
                 matrix[1]=> matrix[2][1], matrix[1][1], matrix[0][1]
                 matrix[2]=> matrix[2][2], matrix[1][2], matrix[0][2]
                 
        """
        m_copy = matrix.copy()
        print(m_copy)
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[i])):
                a = matrix[j][i]
                matrix[i].append(a)

        for i in range(len(m_copy)):
            a = len(m_copy[i])//2
            print(a)
            matrix[i][:a] = []
            
        for i in matrix:
            i.reverse()

        print(m_copy)
        return matrix
