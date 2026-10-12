class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 0.2
        print(f"{self.name} provides {shade} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe_nutrition(self):
        print(f"{self.name} is {self.nutritional_value}")

def main():
    print("=== Garden Plant Types ===")
    flower = Flower("Rose", 25, 30, "red")
    tree = Tree("Oak", 500, 1825, 50)
    veg = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")

    flower.bloom()
    tree.produce_shade()
    veg.describe_nutrition()

if __name__ == "__main__":
    main()
