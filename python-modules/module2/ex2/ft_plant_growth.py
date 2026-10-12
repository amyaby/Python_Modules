class Plant:
    #constructur
    def __init__(self,name,height,days):
        self.name = name
        self.height = height
        self.days=days
    def grow(self):
        self.height += 2
    def age(self):
        self.days += 170
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.days} days")
def main():
    wheat = Plant("Wheat", 15, 3)
    tomato = Plant("Tomato", 25, 7)
    sesame = Plant("Sesame", 80, 14)

    plants = [wheat, tomato, sesame]
        #for plant in plants:
        #   plant.get_info()

    for day in range(7):
        print(f"\n=== Day {day + 1} ===")

        for plant in plants:
            plant.grow()
            plant.age()
            plant.get_info()
    print(f"growth this week :+{day}cm")

if __name__ == "__main__":
        main()