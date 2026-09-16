"""
Experiment 8.2 - Problem 2: Frog Jump with K Distance
Approach: Brute Force recursion
CC-II (24CSP-339)
"""

from typing import List


class Solution:
    def minCost(self, height: List[int], k: int) -> int:
        n = len(height)

        def solve(i):
            if i == 0:
                return 0
            best = float("inf")
            for j in range(max(0, i - k), i):
                best = min(best, solve(j) + abs(height[i] - height[j]))
            return best

        return solve(n - 1)


if __name__ == "__main__":
    print("=" * 64)
    print("  FROG JUMP WITH K DISTANCE  |  Brute Force Recursion")
    print("  Experiment 8.2")
    print("=" * 64)
    print()

    sol = Solution()
    cases = [
        ([10, 30, 40, 50, 20], 3),
        ([10, 20, 10], 1),
        ([30, 10, 60, 10, 60, 50], 2),
        ([40], 1),
        ([10, 10, 10, 10], 3),
    ]

    for height, k in cases:
        print(f"height = {height}, k = {k}")
        print(f"  Min cost : {sol.minCost(height, k)}")
        print()

    print("=" * 64)
    print("  All test cases executed successfully.")
    print("=" * 64)
