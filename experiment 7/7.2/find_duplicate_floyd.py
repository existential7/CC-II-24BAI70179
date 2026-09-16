"""
Experiment 7.2 - Problem 2: Find the Duplicate Number
Approach: Floyd's tortoise and hare (cycle detection)
LeetCode #287 | CC-II (24CSP-339)
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == "__main__":
    print("=" * 64)
    print("  FIND THE DUPLICATE NUMBER  |  Floyd Cycle Detection")
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
