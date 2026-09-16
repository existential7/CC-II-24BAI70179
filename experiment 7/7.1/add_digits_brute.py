"""
Experiment 7.1 - Problem 1: Add Digits
Approach: Brute Force simulation (repeated digit sums)
LeetCode #258 | CC-II (24CSP-339)
"""


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
        return num


if __name__ == "__main__":
    print("=" * 64)
    print("  ADD DIGITS  |  Brute Force (simulate digit sums)")
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
