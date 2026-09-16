"""
Experiment 6.2 - Problem 2: Inorder Successor in BST
Approach: Optimized iterative BST walk O(h)
LeetCode #285 | CC-II (24CSP-339)
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
    def inorderSuccessor(self, root: "TreeNode", p: "TreeNode") -> "TreeNode":
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor


if __name__ == "__main__":
    print("=" * 64)
    print("  INORDER SUCCESSOR IN BST  |  Iterative BST Walk")
    print("  LeetCode #285  |  Experiment 6.2")
    print("=" * 64)
    print()

    sol = Solution()
    cases = [
        ([2, 1, 3], 1),
        ([5, 3, 6, 2, 4, "#", "#", 1], 6),
        ([5, 3, 6, 2, 4, "#", "#", 1], 3),
        ([2, 1, 3], 2),
        ([5, 3, 6, 2, 4, "#", "#", 1], 2),
    ]

    for tree_vals, pval in cases:
        root = build_tree(tree_vals)
        p = find_node(root, pval)
        ans = sol.inorderSuccessor(root, p)
        print(f"BST (level-order): {tree_vals}")
        print(f"  p = {pval}")
        print(f"  Successor : {ans.val if ans else None}")
        print()

    print("=" * 64)
    print("  All test cases executed successfully.")
    print("=" * 64)
