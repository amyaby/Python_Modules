class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

def plant_factory(raw_plants):
    su = 0
    plants = []
    for name, height, age in raw_plants:
        #plants.append(p) puts the new Plant object into the plants list
        p = Plant(name, height, age)
        plants.append(p)
        su += 1
        print(f"Created: {p.name} ({p.height}cm, {p.age} days old)")
    print(f"Total plants created: {su}")

# no return  # keep if needed, but no return = just build + print
#    return [Plant(name, height, age) for name, height, age in raw_plants]

def main():
    print("=== Plant Factory Output ===")
    raw_plants = [
        ("sesam", 20, 60),
        ("potato", 50, 100),
        ("carrots", 4, 33),
        ("Sunflower",80, 45),
        ("Fern",15, 120), 
    ]
    plant_factory(raw_plants)
if __name__ == "__main__":
    main()
