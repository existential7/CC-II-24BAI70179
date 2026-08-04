# Search in Rotated Sorted Array

This repository contains Python implementations of different approaches to solve the **Search in Rotated Sorted Array** problem.

## Files

| File | Description |
|------|-------------|
| `bruteForce.py` | Searches the array sequentially using the Linear Search approach. Time Complexity: **O(n)**. |
| `binarySearch.py` | Searches the target using Binary Search on a rotated sorted array. Time Complexity: **O(log n)**. |

## Approaches

### 1. Brute Force
- Traverses each element one by one.
- Returns the index if the target is found.
- Easy to understand and implement.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

### 2. Binary Search
- Uses Binary Search to locate the target in a rotated sorted array.
- Determines which half of the array is sorted during each iteration.
- Narrows the search space accordingly.

**Time Complexity:** `O(log n)`  
**Space Complexity:** `O(1)`

## Example

**Input**

```text
nums = [4,5,6,7,0,1,2]
target = 0
```

**Output**

```text
4
```

## Screenshots

### Brute Force Output
![Brute Force](bruteForce.png)

### Binary Search Output
![Binary Search](binarySearch.png)

## Language

- Python 3

## How to Run

Run the brute force solution:

```bash
python bruteForce.py
```

Run the binary search solution:

```bash
python binarySearch.py
```

## Purpose

This repository demonstrates two approaches for solving the **Search in Rotated Sorted Array** problem:

- **Brute Force** for simplicity and understanding.
- **Binary Search** for the optimal `O(log n)` solution commonly used in coding interviews.