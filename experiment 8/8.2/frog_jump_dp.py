"""
Experiment 8.2 - Problem 2: Frog Jump with K Distance
Approach: Bottom-up 1-D DP
CC-II (24CSP-339)
"""

from typing import List


class Solution:
    def minCost(self, height: List[int], k: int) -> int:
        n = len(height)
        dp = [0] * n
        for i in range(1, n):
            best = float("inf")
            for j in range(max(0, i - k), i):
                cost = dp[j] + abs(height[i] - height[j])
                best = min(best, cost)
            dp[i] = best
        return dp[n - 1]


if __name__ == "__main__":
    print("=" * 64)
    print("  FROG JUMP WITH K DISTANCE  |  Bottom-Up 1-D DP")
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
