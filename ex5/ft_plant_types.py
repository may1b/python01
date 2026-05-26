class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def grow(self):
        self._height += 2.1

    def age(self):
        self._age += 1

    def show(self):
        print(f"{self._name}: {round(self._height, 1)}cm,"
              f" {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False

    def bloom(self):
        self._blooming = True

    def show(self):
        super().show()
        print(f"Color: {self._color}")
        if self._blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self):
        super().grow()
        self._nutritional_value += 1

    def show(self):
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def main():
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
