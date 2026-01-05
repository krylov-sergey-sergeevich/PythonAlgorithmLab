from collections import defaultdict, Counter
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        d = {}
        for el in nums:
            d[el] = d.get(el, 0) + 1
        for k,v in d.items():
            if v == n:
                return k

class Solution2:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        d = defaultdict(int)
        for el in nums:
            d[el] += 1
        for k, v in d.items():
            if v == n:
                return k

class Solution3:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        counts = Counter(nums)
        for k, v in counts.items():
            if v == n:
                return k

if __name__ == "__main__":
    solution = Solution()
    print(solution.repeatedNTimes([1,2,3,3]))
    print(solution.repeatedNTimes([2,1,2,5,3,2]))
    print(solution.repeatedNTimes([5,1,5,2,5,3,5,4]))