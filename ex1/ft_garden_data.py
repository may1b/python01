class Plant:
    _name: str
    _height: int  # in cm
    _age: int  # in days

    def show(self) -> None:
        day_s = "days" if self._age > 1 else "day"
        print(f"{self._name}: {self._height}cm, {self._age} {day_s} old")


def main() -> None:
    rose = Plant()
    rose._name = "Rose"
    rose._height = 25
    rose._age = 30

    sunflower = Plant()
    sunflower._name = "Sunflower"
    sunflower._height = 80
    sunflower._age = 45

    cactus = Plant()
    cactus._name = "Cactus"
    cactus._height = 15
    cactus._age = 120

    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
