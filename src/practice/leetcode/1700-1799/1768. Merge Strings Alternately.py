from src.tools.AssertUtils import check


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        while i < len(word1) and i < len(word2):
            result += word1[i]
            result += word2[i]
            i += 1
        result += word1[i:]
        result += word2[i:]
        return result


if __name__ == "__main__":
    solution = Solution()
    check(solution.mergeAlternately("abc", "pqr"), "apbqcr")
    check(solution.mergeAlternately("ab", "pqrs"), "apbqrs")
    check(solution.mergeAlternately("abcd", "pq"), "apbqcd")
