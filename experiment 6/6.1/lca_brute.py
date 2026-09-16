"""
Experiment 6.1 - Problem 1: Lowest Common Ancestor of a Binary Tree
Approach: Brute Force (store two root-to-node paths)
LeetCode #236 | CC-II (24CSP-339)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(vals: List) -> Optional[TreeNode]:
    """Build a binary tree from level-order list. None / '#' = missing child."""
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
        def path(node, target, trail):
            if node is None:
                return False
            trail.append(node)
            if node is target or node.val == target.val:
                return True
            if path(node.left, target, trail) or path(node.right, target, trail):
                return True
            trail.pop()
            return False

        path1, path2 = [], []
        path(root, p, path1)
        path(root, q, path2)
        i = 0
        while i < len(path1) and i < len(path2) and path1[i] is path2[i]:
            i += 1
        return path1[i - 1]


if __name__ == "__main__":
    print("=" * 64)
    print("  LCA OF BINARY TREE  |  Brute Force (two paths)")
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
