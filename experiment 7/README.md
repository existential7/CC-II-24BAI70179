# Experiment 7 — Math and Cycle Detection

**Subject:** CC-II (24CSP-339)

| Folder | Experiment | Problem |
|--------|------------|---------|
| `7.1/` | 2.3.1 | LeetCode #258 Add Digits |
| `7.2/` | 2.3.2 | LeetCode #287 Find the Duplicate Number |

## 7.1 Add Digits

| File | Description |
|------|-------------|
| `add_digits_brute.py` | Simulate repeated digit sums |
| `add_digits_formula.py` | O(1) digital-root formula `1 + (num-1) % 9` |
| `output_brute.jpg` | Console output of the simulation |
| `output_formula.jpg` | Console output of the formula |

```bash
python3 add_digits_brute.py
python3 add_digits_formula.py
```

## 7.2 Find the Duplicate Number

| File | Description |
|------|-------------|
| `find_duplicate_brute.py` | Hash-set scan |
| `find_duplicate_floyd.py` | Floyd tortoise-and-hare, O(1) extra space |
| `output_brute.jpg` | Console output of the hash-set program |
| `output_floyd.jpg` | Console output of Floyd's algorithm |

```bash
python3 find_duplicate_brute.py
python3 find_duplicate_floyd.py
```
