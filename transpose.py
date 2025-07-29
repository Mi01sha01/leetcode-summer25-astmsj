from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        transpose_matrix = [[] for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                transpose_matrix[j].append(matrix[i][j])
        
        return transpose_matrix