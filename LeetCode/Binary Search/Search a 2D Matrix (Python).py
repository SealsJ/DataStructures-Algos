class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        row_len = len(matrix)
        col_len = len(matrix[0])

        low = 0
        high = row_len * col_len - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid // col_len][mid % col_len] == target:
                return True
            elif matrix[mid // col_len][mid % col_len] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
