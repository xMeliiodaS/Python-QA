from Task2.animal import Animal


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "The cat mewos"