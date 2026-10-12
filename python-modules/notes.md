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

---

## Module 2 — Exercise Progression (Plant Factory)

| Exercise | File | What it teaches | Key elements |
|---|---|---|---|
| **ex00** | `ft_garden_intro.py` | Basic variables + printing. No class. | `plant = "wheat"`, `height, age = 15, 2`, `print(...)`, `if __name__ == "__main__"` |
| **ex01** | `ft_garden_data.py` | `Plant` **class** to hold data; make instances; loop & print. | `class Plant: def __init__(...)`, `Plant("Wheat", 15, 3)`, list of objects, `for i in plants:` |
| **ex02** | `ft_plant_growth.py` | Add **behaviour** to class (`grow()`, `age()`, `get_info()`); simulate over time (`range(7)`). | Instance methods with `self`, mutation (`self.height += 2`), `range()` loop |
| **ex03** | `ft_plant_factory.py` | **Factory pattern**: a function that takes raw data (tuples) and builds `Plant` objects. Focus = **object creation**, not mutation. | `def plant_factory(...): return [Plant(...) ...]`, hardcoded or `input()` data, `get_info()` display |

### Factory idea (ex03 vs ex02)
- **ex02**: you *already have* objects (created inline like `Plant("Wheat", 15, 3)`); you then change them with methods (`grow`, `age`).
- **ex03**: you *create* objects from raw data (tuples / list). The class defines *what a plant is*; the factory defines *how to build one*.

#### Why not just write each `Plant(...)` line?
If you hard-code:
```python
wheat = Plant("Wheat", 15, 3)
tomato = Plant("Tomato", 25, 7)
sesame = Plant("Sesame", 80, 14)
```
you lose the ability to:
1. **Change the data source** without touching the creation logic (e.g., read from a file or `input()`).
2. **Reuse the creation logic** elsewhere (another module, a test, etc.).
3. **Scale** to dozens or hundreds of plants—you’d have to write hundreds of lines.
4. **Separate concerns**: the class says *what a Plant is*; the factory says *how to turn raw data into Plants*.

The factory pattern keeps `main()` (or any caller) focused on **what** it needs (`give me Plant objects for this data`) while the factory handles **how** (call the constructor for each tuple). This becomes valuable as programs grow.

---

Concept: Classes in Python

Class Definition Syntax

class ClassName:
    # class body
    pass
__init__ Method (constructor)

class Plant:
    def __init__(self, name, height, age):
        self.name = name      # self.variable = parameter
        self.height = height
        self.age = age
Instance Methods

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    
    def display(self):          # method = function inside class
        return f"{self.name}: {self.height}cm, {self.age} days"
Create & Use Objects

rose = Plant("Rose", 25, 30)   # create instance
print(rose.display())          # call method via object
Key Concepts:

self = the current instance (like this in other languages)
self.variable = instance attribute
Methods receive self as first implicit parameter
Instance created with ClassName(args)

What's the difference?

Inside your class, you write the method definition:

def get_info(self):
    print(f"{self.name}: {self.height}cm")

Here, self is a parameter. It represents the particular object whose information you want to display.

When you call the method, you write:

wheat.get_info()

You don't pass self manually. Python automatically passes wheat as the first argument.

Conceptually, Python treats this call like:

Plant.get_info(wheat)