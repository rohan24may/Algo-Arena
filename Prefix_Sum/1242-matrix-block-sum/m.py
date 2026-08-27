class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]: # pyright: ignore[reportUndefinedVariable]

        rows = len(mat)
        cols = len(mat[0])

        # 1. Create prefix matrix
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        # 2. Build 2D prefix sum
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] = (
                    prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                    + mat[i][j]
                )

        # 3. Create answer matrix
        answer = [[0] * cols for _ in range(rows)]

        # 4. Calculate each block sum
        for i in range(rows):
            for j in range(cols):

                top = max(0, i - k)
                bottom = min(rows - 1, i + k)

                left = max(0, j - k)
                right = min(cols - 1, j + k)

                block_sum = (
                    prefix[bottom + 1][right + 1]
                    - prefix[top][right + 1]
                    - prefix[bottom + 1][left]
                    + prefix[top][left]
                )

                answer[i][j] = block_sum

        return answer