# Definition for a binary tree node.
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
    def max(self, node: Optional[TreeNode], sum_all: int) -> int:
        if node is None:
            return 0
        return max(self.max(node.left, sum_all), self.max(node.right, sum_all), (sum_all-node.val)*node.val)

    def convert(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node is None:
            return None
        if node is not None and node.left is None and node.right is None:
            return node
        else:
            l = self.convert(node.left)
            r = self.convert(node.right)
            l_val = l.val if l is not None else 0
            r_val = r.val if r is not None else 0
            return TreeNode(node.val + l_val + r_val, l, r)


    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tree = self.convert(root)
        m = self.max(tree, tree.val)
        return m % (10**9 + 7)

if __name__ == "__main__":
    solution = Solution()
    # Пример [1, 2, 3, 4, 5, 6]
    print(solution.maxProduct(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), None))))
    print(solution.maxProduct(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), None))))