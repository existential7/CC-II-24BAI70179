"""
Experiment 7.1 - Problem 1: Add Digits
Approach: Optimized digital-root formula O(1)
LeetCode #258 | CC-II (24CSP-339)
"""


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9


if __name__ == "__main__":
    print("=" * 64)
    print("  ADD DIGITS  |  Digital Root Formula O(1)")
    print("  LeetCode #258  |  Experiment 7.1")
    print("=" * 64)
    print()

    sol = Solution()
    tests = [38, 0, 5, 99, 12345, 10, 100, 9, 18, 2147483647]

    for num in tests:
        print(f"num = {num}")
        print(f"  Digital root : {sol.addDigits(num)}")
        print()

    print("=" * 64)
    print("  All test cases executed successfully.")
    print("=" * 64)
