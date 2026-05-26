class Plant:
    _name: str
    _height: int  # in cm
    _age: int  # in days

    def __init__(self, name: str, height: int, age: int):
        self._name = name
        self._height = height
        self._age = age

    def show(self):
        day_s = "days" if self._age > 1 else "day"
        print(f"{self._name}: {self._height}cm, {self._age} {day_s} old")


def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
