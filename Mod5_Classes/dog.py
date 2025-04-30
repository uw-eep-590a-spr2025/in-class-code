
class Dog:

    def __init__(self, color):
        self.color = color

    def shed(self):
        print(f'{self.color} Doggy glitter everywhere! ')


    def speak(self):
        print('Arf!')



class Cat():
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        print('Getting the color of the cat')
        return self._color


garfield = Cat('orange')
print(garfield.color)