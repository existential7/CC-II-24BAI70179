"""
Experiment 8.1 - Problem 1: Climbing Stairs
Approach: Brute Force recursion
LeetCode #70 | CC-II (24CSP-339)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == "__main__":
    print("=" * 64)
    print("  CLIMBING STAIRS  |  Brute Force Recursion")
    print("  LeetCode #70  |  Experiment 8.1")
    print("=" * 64)
    print()

    sol = Solution()
    # Recursion is exponential; only small n from the lab table.
    tests = [1, 2, 3, 4, 5, 6, 8, 10]

    for n in tests:
        print(f"n = {n}")
        print(f"  Ways : {sol.climbStairs(n)}")
        print()

    print("=" * 64)
    print("  All test cases executed successfully.")
    print("=" * 64)
