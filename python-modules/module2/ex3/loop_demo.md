=== LOOP SHOWS ONE BY ONE ===

raw_plants = [
    ("sesam", 20, 60),   # tuple 1
    ("potato", 50, 100), # tuple 2
    ("carrots", 4, 33),  # tuple 3
]

Loop runs 3 times (one per tuple):

ITERATION 1:
  name = "sesam"      (1st value from tuple 1)
  height = 20         (2nd value)
  age = 60            (3rd value)
  → makes Plant("sesam", 20, 60) → prints

ITERATION 2:
  name = "potato"     (from tuple 2)
  height = 50
  age = 100
  → makes Plant("potato", 50, 100) → prints

ITERATION 3:
  name = "carrots"
  height = 4
  age = 33
  → makes Plant("carrots", 4, 33) → prints

NOT all at once. Each loop = one tuple = one Plant object.
