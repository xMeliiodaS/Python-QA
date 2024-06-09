from Tasks.rectangle import Rectangle
from Tasks.circle import Circle


def main():

    cir = Circle("Blue", 7)
    rec = Rectangle("Red", 5, 2)

    print(cir.area())
    print(rec.area())


main()