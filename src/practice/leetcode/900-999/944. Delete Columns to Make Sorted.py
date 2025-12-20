from typing import List

from src.tools.AssertUtils import check


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            ord_previous_symbol = 0
            for el in strs:
                #print(f"{ord_previous_symbol} vs {ord(el[i])} {el[i]}")
                if ord_previous_symbol > ord(el[i]):
                    count += 1
                    break
                else:
                    ord_previous_symbol = ord(el[i])
        return count

if __name__ == "__main__":
    solution = Solution()
    check(solution.minDeletionSize(["cba","daf","ghi"]), 1)
    check(solution.minDeletionSize(["a","b"]), 0)
    check(solution.minDeletionSize(["zyx","wvu","tsr"]), 3)