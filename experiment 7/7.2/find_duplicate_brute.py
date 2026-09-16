"""
Experiment 7.2 - Problem 2: Find the Duplicate Number
Approach: Brute Force hash set
LeetCode #287 | CC-II (24CSP-339)
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)
        return -1


if __name__ == "__main__":
    print("=" * 64)
    print("  FIND THE DUPLICATE NUMBER  |  Brute Force (hash set)")
    print("  LeetCode #287  |  Experiment 7.2")
    print("=" * 64)
    print()

    sol = Solution()
    tests = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [3, 3, 3, 3, 3],
        [1, 1],
        [2, 5, 9, 6, 9, 3, 8, 9, 7, 1],
    ]

    for nums in tests:
        print(f"nums = {nums}")
        print(f"  Duplicate : {sol.findDuplicate(nums)}")
        print()

    print("=" * 64)
    print("  All test cases executed successfully.")
    print("=" * 64)
