from typing import Optional
import sys

MAX_SIZE = sys.maxsize  # обычно 2**63 - 1 на 64-битных системах
MIN_SIZE = -sys.maxsize - 1  # соответствующий минимум


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        current_level = []
        next_level = []
        k = 1
        max = MIN_SIZE
        level = -1
        current_level.append(root)
        while len(current_level) != 0:
            s = None
            for el in current_level:
                if el is not None:
                    if s is None:
                        s= el.val
                    else:
                        s += el.val
                    next_level.append(el.left)
                    next_level.append(el.right)
            if s is not None and s > max:
                max = s
                level = k
            current_level = next_level
            next_level = []
            k += 1
        return level


if __name__ == "__main__":
    solution = Solution()
    #print(solution.maxLevelSum(TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))))
    #print(solution.maxLevelSum(TreeNode(989, None, TreeNode(10250, TreeNode(98693), TreeNode(-89388, None, TreeNode(-32127))))))
    print(solution.maxLevelSum(TreeNode(-100, TreeNode(-200, TreeNode(-20), TreeNode(-5)), TreeNode(-300, TreeNode(-10)))))
