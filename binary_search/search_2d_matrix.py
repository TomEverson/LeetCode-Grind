from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top_ptr, bot_ptr = 0, ROWS - 1
        while top_ptr <= bot_ptr:
            row_mid_point = (top_ptr + bot_ptr) // 2
            if target > matrix[row_mid_point][-1]:
                top_ptr = row_mid_point + 1
            elif target < matrix[row_mid_point][0]:
                bot_ptr = row_mid_point - 1
            else:
                break

        left_ptr, right_ptr = 0, COLS - 1
        row_mid_point = (top_ptr + bot_ptr) // 2
        while left_ptr <= right_ptr:
            col_mid_point = (left_ptr + right_ptr) // 2
            if target > matrix[row_mid_point][col_mid_point]:
                left_ptr = col_mid_point + 1
            elif target < matrix[row_mid_point][col_mid_point]:
                right_ptr = col_mid_point - 1
            else:
                return True

        return False


solution = Solution()

print(solution.searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11))
