

class Pet:
    def __init__(self, name, color):
        print('Creating a Pet with name {name} and color {color}'.format(name=name, color=color))
        self.name = name
        self.color = color

class Dog(Pet):
    def __init__(self, name, color):
        print('Creating a Dog with name {name} and color {color}'.format(name=name, color=color))
        super().__init__(name, color)

dubs = Dog('dubs', 'gray')

papi = Pet('papi', 'orange')

