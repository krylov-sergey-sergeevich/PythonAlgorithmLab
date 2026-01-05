from typing import List, Set


class Solution:
    def factor(self, n: int) -> Set[int]:
        ans = set()
        ans.add(n)
        d = 1
        while d * d <= n:
            if n % d == 0:
                ans.add(d)
                ans.add(n // d)
            d += 1
            if len(ans) >= 5:
                return set()
        return ans

    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        res_dict = {}
        for el in nums:
            if res_dict.__contains__(el):
                s += res_dict[el]
            else:
                elements = self.factor(el)
                if len(elements) == 4:
                    sum_elements = sum(elements)
                    s += sum_elements
                    res_dict[el] = sum_elements
                else:
                    res_dict[el] = 0
        return s


if __name__ == '__main__':
    solution = Solution()
    print(solution.sumFourDivisors([21,21]))
