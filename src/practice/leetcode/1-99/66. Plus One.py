from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        k = 1
        for i in range(len(digits)):
            t = digits[i] + k
            digits[i] = t % 10
            k = t // 10
            if k == 0:
                digits.reverse()
                return digits
        digits.reverse()
        return [1] + digits

if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))
    print(solution.plusOne([4,3,2,1]))
    print(solution.plusOne([9]))
