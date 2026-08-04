# Insert Into Array

This repository contains Python implementations of different approaches to solve the **Insert Into Array** problem.

## Files

| File | Description |
|------|-------------|
| `bruteForce.py` | Inserts an element into an array using the straightforward approach by shifting elements manually. Time Complexity: **O(n)**. |
| `lowerBondApproach.py` | Uses the Lower Bound approach to determine the correct insertion position in a sorted array. Time Complexity: **O(log n)** for searching and **O(n)** for insertion. |

## Approaches

### 1. Brute Force
- Traverses the array to the required position.
- Shifts all subsequent elements one position to the right.
- Inserts the new element at the desired index.

**Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

### 2. Lower Bound Approach
- Finds the first position where the element can be inserted while maintaining sorted order.
- Shifts the remaining elements to make space.
- Efficient for determining the insertion index in a sorted array.

**Time Complexity:**
- Lower Bound Search: `O(log n)`
- Element Insertion: `O(n)`
- Overall: `O(n)`

**Space Complexity:** `O(1)`

## Example

**Input**

```text
Array = [1, 3, 5, 7]
Element = 4
```

**Output**

```text
[1, 3, 4, 5, 7]
```

## Screenshots

### Brute Force Output
![Brute Force](Bruteforce.png)

### Lower Bound Approach Output
![Lower Bound Approach](lowerBondApproach.png)

### Binary Insert Output
![Binary Insert](binaryInsert.png)

## Language

- Python 3

## How to Run

Run the brute force solution:

```bash
python bruteForce.py
```

Run the Lower Bound solution:

```bash
python lowerBondApproach.py
```

## Purpose

This repository demonstrates two approaches for solving the **Insert Into Array** problem:

- **Brute Force** for understanding the basic insertion process.
- **Lower Bound Approach** for efficiently determining the insertion position in a sorted array before performing the insertion.