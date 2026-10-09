# Python Module Notes

## General Notes

### `input()`
`input()` returns a **string**, so numeric input must be converted:
```python
days = int(input("Days until harvest: "))   # string -> int
```

### `range()`
- `range(start, stop)` → iterations **start from `start`** and stop before `stop`
  ```python
  range(1, 6)   # 1, 2, 3, 4, 5
  ```
- `range(stop)` → starts from **0**
  ```python
  range(5)      # 0, 1, 2, 3, 4  (commence de 0)
  ```

### Testing
To test a function, either call it directly:
```bash
python -c "from ft_harvest_total import ft_harvest_total; ft_harvest_total()"
```
or use a `main()` entry point:
```python
def main():
    res = ft_plot_area()
    # print(res)

if __name__ == "__main__":
    main()
```

---

## Function Signatures & Type Annotations

Python lets you annotate the types of parameters and the return value.

### Syntax
```python
def function_name(parameter1: type, parameter2: type) -> return_type:
    # Your code
```

### Example 1: returns a value
```python
def add(a: int, b: int) -> int:
    return a + b
```
This function **returns** an integer.

### Example 2: returns nothing
```python
def display(message: str) -> None:
    print(message)
```
This function **displays** a message but returns nothing (`None`).

### Key distinction
- `-> <type>` → what the function gives back
- `-> None` → the function does not return a value (only performs an action)

---

## Recursion

**Recursion**: a function that calls itself.

### Recursive Pattern
```python
def function(something):
    if STOP_CONDITION:      # base case
        return

    # do something

    function(smaller_or_next_value)   # recursive step
```

---

## Function `ft_count_harvest_recursive()` — Role of `count(1)`

In the recursive function `ft_count_harvest_recursive()`, the line `count(1)` is the **initial invocation** of the nested helper function `count(day)`.

### What `count(1)` Does
- Seeds the recursion with the first day to display (day 1).
- The helper `count(day)` then:
  1. Checks the **base case**: if `day > days`, print `"Harvest time!"` and return (stop recursing).
  2. Otherwise, prints `Day {day}` and calls itself with the next day: `count(day + 1)` (recursive step).
- This builds the counting sequence from day 1 up to the user-specified number of days.

### Why Start at `1`?
- The program's purpose is to count days **from 1 to N** (N = user input).
- `count(0)` → would include an unwanted `Day 0`.
- `count(2)` → would skip Day 1 entirely.
- `count(1)` → gives the correct sequence: Day 1, Day 2, ..., Day N.

### Example Execution (user enters `3`)
| Step | Call        | Action                                  |
|------|-------------|-----------------------------------------|
| 1    | `count(1)`  | 1 > 3? No → print `Day 1`, call `count(2)` |
| 2    | `count(2)`  | 2 > 3? No → print `Day 2`, call `count(3)` |
| 3    | `count(3)`  | 3 > 3? No → print `Day 3`, call `count(4)` |
| 4    | `count(4)`  | 4 > 3? **Yes** → print `Harvest time!`, return |
| 5    | —           | Stack unwinds: `count(3)` → `count(2)` → `count(1)` return |

**Output:**
```
Day 1
Day 2
Day 3
Harvest time!
```

### Key Takeaway
`count(1)` **kicks off the recursive day-counting process at the correct starting point** (day 1). Without this initial call, the recursive function would never execute, and the program would terminate after asking for input without producing any counting output.