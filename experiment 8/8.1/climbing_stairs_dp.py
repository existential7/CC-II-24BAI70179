"""
Experiment 8.1 - Problem 1: Climbing Stairs
Approach: Bottom-up DP with two rolling variables
LeetCode #70 | CC-II (24CSP-339)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev1, prev2 = 1, 2
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current
        return prev2


if __name__ == "__main__":
    print("=" * 64)
    print("  CLIMBING STAIRS  |  Bottom-Up DP (O(n) / O(1))")
    print("  LeetCode #70  |  Experiment 8.1")
    print("=" * 64)
    print()

    sol = Solution()
    tests = [1, 2, 3, 4, 5, 6, 8, 10, 20, 45]

    for n in tests:
        print(f"n = {n}")
        print(f"  Ways : {sol.climbStairs(n)}")
        print()

    print("=" * 64)
    print("  All test cases executed successfully.")
    print("=" * 64)
