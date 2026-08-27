class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        rows = len(mat)
        cols = len(mat[0])

        answer = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):

                block_sum = 0

                for r in range(max(0, i - k), min(rows, i + k + 1)):
                    for c in range(max(0, j - k), min(cols, j + k + 1)):
                        block_sum += mat[r][c]

                answer[i][j] = block_sum

        return answer