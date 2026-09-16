"""
Experiment 6.1 - Problem 1: Lowest Common Ancestor of a Binary Tree
Approach: Optimized single-pass DFS
LeetCode #236 | CC-II (24CSP-339)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals: List) -> Optional[TreeNode]:
    if not vals:
        return None
    nodes = []
    for v in vals:
        if v is None or v == "#":
            nodes.append(None)
        else:
            nodes.append(TreeNode(v))
    i = 0
    child = 1
    while child < len(nodes):
        if nodes[i] is not None:
            if child < len(nodes):
                nodes[i].left = nodes[child]
                child += 1
            if child < len(nodes):
                nodes[i].right = nodes[child]
                child += 1
        i += 1
    return nodes[0]


def find_node(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        if root is None or root is p or root is q or root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right


if __name__ == "__main__":
    print("=" * 64)
    print("  LCA OF BINARY TREE  |  Single-Pass DFS")
    print("  LeetCode #236  |  Experiment 6.1")
    print("=" * 64)
    print()

    sol = Solution()
    cases = [
        ([3, 5, 1, 6, 2, 0, 8, "#", "#", 7, 4], 5, 1),
        ([3, 5, 1, 6, 2, 0, 8, "#", "#", 7, 4], 5, 4),
        ([1, 2], 1, 2),
        ([3, 5, 1, 6, 2, 0, 8], 6, 8),
        ([3, 5, 1, 6, 2, 0, 8, "#", "#", 7, 4], 7, 4),
    ]

    for tree_vals, pval, qval in cases:
        root = build_tree(tree_vals)
        p = find_node(root, pval)
        q = find_node(root, qval)
        ans = sol.lowestCommonAncestor(root, p, q)
        print(f"Tree (level-order): {tree_vals}")
        print(f"  p = {pval}, q = {qval}")
        print(f"  LCA  : {ans.val if ans else None}")
        print()

    print("=" * 64)
    print("  All test cases executed successfully.")
    print("=" * 64)
