class Plant:
    name: str
    height: int  # in cm
    age: int  # in days

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        day_s = "days" if self.age > 1 else "day"
        print(f"{self.name}: {self.height}cm, {self.age} {day_s} old")


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
