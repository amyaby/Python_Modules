class Plant:
    #constructur
    def __init__(self,name,height,age):
        self.name = name
        self.height = height
        self.age=age
def  ft_garden_data():
    wheat = Plant("Wheat",15,3)
    tomato = Plant("Tomato", 25, 7)
    sesame = Plant("Sesame", 80, 14)
    plants = [wheat,tomato,sesame]
    for i in plants:
            print("=== Garden Plant Data ===")
            print(f"{i.name}: {i.height}cm, {i.age} days old")
#def main():
#    ft_garden_data()
#if __name__ == "__main__":
#    main()