class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat_list = sum(mat, [])
        new_len = len(mat)* len(mat[0])
        if r*c == new_len: 
            return [flat_list[i:i+c]for i in range(0 , new_len, c)]
        else:
            return mat