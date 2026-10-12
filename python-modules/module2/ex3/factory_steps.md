=== How Factory Works ===
main() starts with raw data (tuples):
  raw_plants = [("sesam",20,60),("potato",50,100),("carrots",4,33)]

plant_factory() loops with unpacking:
  for name, height, age in raw_plants:
      -> Plant(name, height, age)

Why unpacking? Because Plant.__init__ expects those in order.
Tuple order must match constructor order.

Constructor reminder:
  __init__(self, name, height, age) creates object and saves data.

Streamline meaning: instead of Plant(...) 3 times by hand,
we put it in one function for any number of tuples.

Purpose: create many objects from class from raw data list.
