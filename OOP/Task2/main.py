from Task2.animal import Animal
from Task2.cat import Cat
from Task2.dog import Dog


def main():
    animal_a = Animal("v")
    cat_a = Cat("Koko")
    dog_a = Dog("Riro")

    print(animal_a.speak())
    print(cat_a.speak())
    print(dog_a.speak())


if __name__ == '__main__':
    main()