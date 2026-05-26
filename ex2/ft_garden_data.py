class Plant:
    _name: str
    _height: float  # in cm
    _age: int  # in days

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
    starting_height = 25.0
    rose = Plant()
    rose._name = "Rose"
    rose._height = starting_height
    rose._age = 30

    print("=== Garden Plant Growth ===")

    day = 1
    while day <= 7:
        print(f"=== Day {day} ===")
        rose.show()
        rose.age_and_grow()
        day += 1

    print(f"Growth this week: {round(rose._height - starting_height)}cm")


if __name__ == "__main__":
    main()
