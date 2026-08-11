# Stack and Queue Implementation using Different Data Structures

This repository contains Python implementations of **Stack and Queue** data structures using different approaches.

The goal is to understand how one data structure can be implemented using another data structure while maintaining the required behavior.

## Files

| File | Description |
|------|-------------|
| `queue_using_2Stack.py` | Implements Queue using two Stacks. Uses two stacks to achieve FIFO behavior. |
| `queue_using_Stack.py` | Implements Queue using a single Stack. |
| `stack_using_2Queue.py` | Implements Stack using two Queues. Uses two queues to achieve LIFO behavior. |
| `stack_using_Queue.py` | Implements Stack using a single Queue. |

## Approaches

## 1. Queue Using Two Stacks

- Uses two stacks:
  - `stack1` for input operations.
  - `stack2` for output operations.
- Elements are transferred from one stack to another to reverse the order.
- Follows **FIFO (First In First Out)** behavior.

**Operations:**

| Operation | Time Complexity |
|-----------|----------------|
| Push | O(1) |
| Pop | Amortized O(1) |
| Peek | Amortized O(1) |
| Empty | O(1) |

---

## 2. Queue Using One Stack

- Uses recursion to reverse the stack order.
- The newest element is moved to the bottom to maintain queue behavior.
- Follows **FIFO** order.

**Time Complexity:**

- Push: O(n)
- Pop: O(1)

---

## 3. Stack Using Two Queues

- Uses two queues:
  - `q1` stores the current stack elements.
  - `q2` is used temporarily during insertion.
- The newest element is always kept at the front.
- Follows **LIFO (Last In First Out)** behavior.

**Operations:**

| Operation | Time Complexity |
|-----------|----------------|
| Push | O(n) |
| Pop | O(1) |
| Top | O(1) |
| Empty | O(1) |

---

## 4. Stack Using One Queue

- Uses a single queue.
- After inserting a new element, previous elements are rotated behind it.
- Maintains stack order using queue operations.

**Time Complexity:**

| Operation | Complexity |
|-----------|------------|
| Push | O(n) |
| Pop | O(1) |
| Top | O(1) |
| Empty | O(1) |

---

## Examples

### Queue Example

Input:

```text
push(2)
push(43)
push(24)
pop()
```

Output:

```text
2
```

Queue follows:

```text
First In → First Out
```

---

### Stack Example

Input:

```text
push(2)
push(43)
push(24)
pop()
```

Output:

```text
24
```

Stack follows:

```text
Last In → First Out
```

---

## Screenshots

### Queue Using Two Stacks
![Queue To 2 Stack](queue_using_2Stack.png)

### Queue Using Stack
![Queue To Stack](queue_using_Stack.png)

### Stack Using Two Queues
![Stack To 2 Queue](stack_using_2queue.png)

### Stack Using Queue
![Stack To Queue](stack_using_queue.png)

---

## Language

- Python 3

---

## How to Run

Run Queue using Two Stacks:

```bash
python queue_using_2Stack.py
```

Run Queue using Stack:

```bash
python queue_using_Stack.py
```

Run Stack using Two Queues:

```bash
python stack_using_2Queue.py
```

Run Stack using Queue:

```bash
python stack_using_Queue.py
```

---

## Purpose

This repository demonstrates different ways to implement **Stack and Queue** operations by using other data structures.

It covers:
- FIFO implementation using stacks.
- LIFO implementation using queues.
- Understanding data structure behavior.
- Comparing different approaches and their time complexities.