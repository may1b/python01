class Plant:
    class _Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, {self.show_calls} show")

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
        self._stats = Plant._Stats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self):
        self._height += 2.1
        self._stats.grow_calls += 1

    def age(self):
        self._age += 1
        self._stats.age_calls += 1

    def show(self):
        print(f"{self._name}: {round(self._height, 1)}cm,"
              f" {self._age} days old")
        self._stats.show_calls += 1

    def display_stats(self):
        self._stats.display()


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
    class _TreeStats(Plant._Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

        def display(self):
            super().display()
            print(f"{self.shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree._TreeStats()

    def produce_shade(self):
        print(f"Tree {self._name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self._trunk_diameter, 1)}cm wide.")
        self._stats.shade_calls += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str,
                 seeds: int = 0):
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def show(self):
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant):
    print(f"[statistics for {plant._name}]")
    plant.display_stats()


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    for _ in range(20):
        sunflower.age()
    sunflower.bloom()
    sunflower._seeds = 42
    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")
    anon = Plant.anonymous()
    anon.show()
    display_statistics(anon)


if __name__ == "__main__":
    main()
