# Experiment 8 — Dynamic Programming

**Subject:** CC-II (24CSP-339)

| Folder | Experiment | Problem |
|--------|------------|---------|
| `8.1/` | 3.1.1 | LeetCode #70 Climbing Stairs |
| `8.2/` | 3.1.2 | Frog Jump with K Distance |

## 8.1 Climbing Stairs

| File | Description |
|------|-------------|
| `climbing_stairs_brute.py` | Naive recursion `ways(n)=ways(n-1)+ways(n-2)` |
| `climbing_stairs_dp.py` | Bottom-up DP, two rolling variables |
| `output_brute.jpg` | Console output (small n) |
| `output_dp.jpg` | Console output including n = 45 |

```bash
python3 climbing_stairs_brute.py
python3 climbing_stairs_dp.py
```

## 8.2 Frog Jump with K Distance

| File | Description |
|------|-------------|
| `frog_jump_brute.py` | Recurse over previous k stones |
| `frog_jump_dp.py` | 1-D table `dp[i] = min over last k` |
| `output_brute.jpg` | Console output of recursion |
| `output_dp.jpg` | Console output of DP |

```bash
python3 frog_jump_brute.py
python3 frog_jump_dp.py
```
