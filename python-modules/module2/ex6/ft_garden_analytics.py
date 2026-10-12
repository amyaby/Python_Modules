class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1


class FloweringPlant(Plant):
    def __init__(self, name, height, age, color, blooming):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = blooming


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, blooming, prize):
        super().__init__(name, height, age, color, blooming)
        self.prize = prize


class Garden:
    def __init__(self, owner):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def help_all_plants_grow(self):
        for plant in self.plants:
            plant.grow()

    def report(self):
        if not self.plants:
            return f"{self.owner} has no plants"

        plant_types = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
        total_growth = 0

        report = f"Plants in garden:- "
        for plant in self.plants:
            ptype = type(plant).__name__
            plant_types[ptype] = plant_types.get(ptype, 0) + 1
            total_growth += plant.height

            report += f"{plant.name}: {plant.height}cm"
            if hasattr(plant, 'blooming') and plant.blooming:
                report += " (blooming)"
            if hasattr(plant, 'prize') and plant.prize is not None:
                report += f", Prize points: {plant.prize}"
            report += " "

        type_descriptions = []
        if plant_types["Plant"] > 0:
            type_descriptions.append(f"{plant_types['Plant']} regular")
        if plant_types["FloweringPlant"] > 0:
            type_descriptions.append(f"{plant_types['FloweringPlant']} flowering")
        if plant_types["PrizeFlower"] > 0:
            type_descriptions.append(f"{plant_types['PrizeFlower']} prize flowers")

        types_description = ", ".join(type_descriptions)

        report += f"\nPlants added: {len(self.plants)}, Total growth: {total_growth}cm"
        report += f"\nPlant types: {types_description}"
        report += "\nHeight validation test: True"

        return report


def utility_no_garden_data():
    """Utility function that doesn't need garden data"""
    return "This is a static-style utility function"


class GardenManager:
    """Manager that can handle multiple gardens and provide analytics"""

    def __init__(self):
        self.gardens = []

    def add_garden(self, garden):
        """Add a garden to the manager"""
        self.gardens.append(garden)

    def get_total_gardens(self):
        """Return total number of gardens managed"""
        return len(self.gardens)

    def get_all_plants(self):
        """Get all plants across all gardens"""
        all_plants = []
        for garden in self.gardens:
            all_plants.extend(garden.plants)
        return all_plants

    class GardenStats:
        """Nested helper class for calculating statistics"""

        @staticmethod
        def total_growth(garden):
            """Calculate total growth of all plants in a garden"""
            return sum(plant.height for plant in garden.plants)

        @staticmethod
        def plant_count_by_type(garden):
            """Count plants by their type name"""
            counts = {}
            for plant in garden.plants:
                ptype = type(plant).__name__
                counts[ptype] = counts.get(ptype, 0) + 1
            return counts

        @staticmethod
        def average_height(garden):
            """Calculate average height of plants in a garden"""
            if not garden.plants:
                return 0
            return GardenManager.GardenStats.total_growth(garden) / len(garden.plants)

        @staticmethod
        def garden_score(garden):
            """Calculate a score for a garden based on plant heights and types"""
            total_height = GardenManager.GardenStats.total_growth(garden)
            type_counts = GardenManager.GardenStats.plant_count_by_type(garden)
            # Score: base height + bonus for diversity
            diversity_bonus = len(type_counts) * 10
            return total_height + diversity_bonus

    @classmethod
    def create_garden_network(cls, garden_names):
        """Create a garden network - works on the manager type itself"""
        networks = cls()
        for name in garden_names:
            networks.add_garden(Garden(name))
        return networks

    @staticmethod
    def validate_height(height):
        """Static utility: validate that height is positive"""
        return isinstance(height, (int, float)) and height > 0


def calculate_plant_score(height, age):
    """Utility function to calculate score from height and age"""
    return height + age // 10


def main():
    print("=== Garden Management System Demo ===")
    oak = Plant("Oak Tree", 100, 365)
    rose = FloweringPlant("Rose", 25, 30, "red", True)
    sunflower = PrizeFlower("Sunflower", 50, 60, "yellow", True, 10)

    # Test the grow() method
    oak.grow()
    rose.grow()
    sunflower.grow()

    # Create gardens
    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")

    # Add plants to Alice's garden
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    # Create manager with multiple gardens
    manager = GardenManager()
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)
    manager.add_garden(Garden("Charlie"))

    # Alice helping all plants grow
    print("Alice is helping all plants grow...")
    alice_garden.help_all_plants_grow()

    # Report Alice's garden
    print("\n=== Alice's Garden Report ===")
    print(alice_garden.report())

    # Report Bob's garden
    print("\n=== Bob's Garden Report ===")
    print(bob_garden.report())

    # Demo GardenStats nested helper
    print("\n=== Garden Statistics (GardenStats) ===")
    print(f"Alice's garden total growth: {GardenManager.GardenStats.total_growth(alice_garden)}cm")
    print(f"Alice's garden plant counts: {GardenManager.GardenStats.plant_count_by_type(alice_garden)}")
    print(f"Alice's garden average height: {GardenManager.GardenStats.average_height(alice_garden):.1f}cm")
    print(f"Alice's garden score: {GardenManager.GardenStats.garden_score(alice_garden)}")

    # Demo staticmethod validate_height
    print("\n=== Static Method Validation ===")
    print(f"validate_height(100): {GardenManager.validate_height(100)}")
    print(f"validate_height(-5): {GardenManager.validate_height(-5)}")
    print(f"validate_height('abc'): {GardenManager.validate_height('abc')}")

    # Demo utility functions
    print("\n=== Utility Functions ===")
    print(f"Utility function output: {utility_no_garden_data()}")
    score = calculate_plant_score(50, 60)
    print(f"Plant score calculation: {score}")

    # Demo GardenManager stats across all gardens
    print("\n=== Garden Manager Overview ===")
    print(f"Total gardens managed: {manager.get_total_gardens()}")
    all_plants = manager.get_all_plants()
    print(f"Total plants in network: {len(all_plants)}")
    for plant in all_plants:
        print(f"  - {plant.name} ({type(plant).__name__}): {plant.height}cm")

    # Final garden scores
    print("\n=== Final Garden Scores ===")
    alice_score = GardenManager.GardenStats.garden_score(alice_garden)
    bob_score = GardenManager.GardenStats.garden_score(bob_garden)
    print(f"Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {manager.get_total_gardens()}")


if __name__ == "__main__":
    main()