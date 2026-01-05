from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        count_negative = 0
        min_element = abs(matrix[0][0])
        s = 0
        for row in matrix:
            for el in row:
                s += abs(el)
                if el < 0:
                    count_negative += 1
                if abs(el) < min_element:
                    min_element = abs(el)

        if count_negative % 2 == 0:
            return s
        else:
            s -= 2 * min_element
            return s

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxMatrixSum([[1,-1],[-1,1]]))
    print(solution.maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]))