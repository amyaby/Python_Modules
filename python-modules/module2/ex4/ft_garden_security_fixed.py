class SecurePlant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if height < 0:
            print("Error: Height cannot be negative!")
        else:
            self._height = height
            print(f"Height updated to {self._height}cm")

    def set_age(self, age):
        if age < 0:
            print("Error: Age cannot be negative!")
        else:
            self._age = age
            print(f"Age updated to {self._age} days")


def main():
    rose = SecurePlant("Rose", 25, 30)
    print(f"Initial age: {rose.get_age()}")
    rose.set_age(5)
    print(f"After set 5: {rose.get_age()}")
    rose.set_age(-5)
    print(f"After bad -5: {rose.get_age()}")
    rose.set_height(-10)
    print(f"Height after bad -10: {rose.get_height()}")


if __name__ == "__main__":
    main()
