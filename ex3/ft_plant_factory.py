class Plant:
    _name: str
    _height: float  # in cm
    _age: int  # in days

    def __init__(self, name: str, height: float, age: int):
        print(f"Created: {name}: {height}cm, {age} days old")
        self._name = name
        self._height = height
        self._age = age

    def show(self):
        day_s = "days" if self._age > 1 else "day"
        print(f"{self._name}: {round(self._height, 1)}cm,\
 {self._age} {day_s} old")

    def grow(self):
        self._height += 0.8

    def age(self):
        self._age += 1

    def age_and_grow(self):
        self.grow()
        self.age()


def main():
    print("=== Plant Factory Output ===")
    plants = {}  # using dict so flake8 does not complain
    plants["rose"] = Plant("Rose", 25.0, 30)
    plants["oak"] = Plant("Oak", 200.0, 365)
    plants["cactus"] = Plant("Cactus", 5.0, 90)
    plants["sunflower"] = Plant("Sunflower", 80.0, 45)
    plants["fern"] = Plant("Fern", 15.0, 120)


if __name__ == "__main__":
    main()
