from abc import ABC, abstractmethod

class Animals(ABC):                      # A class with both abstract and concrete methods are called as Abstract classes

    def __init__(self):
        self.eyes = 2
        self.is_living = True
        self.legs = 4
        self.sound = 'no'

    def typeOfAnimal(self):
        print("It is a herbivorous animal.")

    @abstractmethod
    def setsound(self, sound):
        pass

    @abstractmethod
    def getsound(self):
        pass

class Interface(ABC):                      # A class with only abstractmethods and no concrete methods are called as Interface classes.
    
    @abstractmethod
    def attackHumans(self):
        pass

    @abstractmethod
    def is_extinct(self):
        pass


class Cat(Animals):
    
    def eats(self):
        print('It likes to eats meat and fish')

class Lion(Interface, Cat):                    # Heirarchical inhertance from Cat which inherits from Animals

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def color(self):
        print("Color of Lion is Grayish Yellow!")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A lion makes " + self.sound + " sound.")

    def typeOfAnimal(self):
        print("Lion is a carnivorous animal")

    def attackHumans(self):
        print("A Lion may attack humans if it is hungry and humans are around it.")

    def is_extinct(self):
        print("No, Lion is not extinct.")

    def get_lifespan(self):
        return self.lifespan


class Tiger(Interface, Cat):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def color(self):
        print("Color of Tiger is orange with black stripes!")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A tiger makes " + self.sound + " sound.")

    def typeOfAnimal(self):
        print("Tiger is a carnivorous animal")

    def attackHumans(self):
        print("A tiger may attack humans if it is hungry and humans are around it.")

    def is_extinct(self):
        print("No, Tiger is not extinct.")

    def get_lifespan(self):
        return self.lifespan

class SaberTooth(Cat, Interface):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    # A virtual method eats()
    def eats(self):                                   # Overriding eats method of the class Cat. Showing Polymorphism.
        print("A saber-tooth cat used to eat meat from other animals!")

    def color(self):
        print("Color of Saber-Tooth was Yellow, Brown, Black, White!")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A Saber-Tooth makes " + self.sound + " sound.")

    def typeOfAnimal(self):
        print("Tiger is a carnivorous animal")

    def attackHumans(self):
        print("A tiger may attack humans if it is hungry and humans are around it.")

    def is_extinct(self):
        print("Yes, Saber Tooth is extinct.")

    def get_lifespan(self):
        return self.lifespan

class Giraffe(Animals, Interface):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def eats(self):
        print("Giraffe eats leaves off the trees!")

    def color(self):
        print("Giraffe has patterns of dark brown, orange, or chestnut spots broken up by white or cream-coloured stripes!")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A Giraffe makes " + self.sound + " sound.")

    def attackHumans(self):
        print("A giraffe is not a harmful animal and is friendly to humans.")

    def is_extinct(self):
        print("No, Giraffe is not extinct.")

    def get_lifespan(self):
        return self.lifespan


class Zebra(Animals, Interface):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def eats(self):
        print("Zebra eat grass!")

    def color(self):
        print("A Zebra has black and white stripes on its body.")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A Zebra makes " + self.sound + " sound.")

    def attackHumans(self):
        print("Zebras are not harmful animals.")

    def is_extinct(self):
        print("No, Zebra is not extinct.")

    def get_lifespan(self):
        return self.lifespan


class Monkey(Animals, Interface):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def eats(self):
        print("Monkey eats vegetables and fruits")

    def color(self):
        print("Color of monkey is brown")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A Monkey makes " + self.sound + " sound.")

    def attackHumans(self):
        print("Monkeys can annoy humans by stealing their food and by pulling their hair. Monkeys are mischevious animals.")

    def is_extinct(self):
        print("No, Monkey is not extinct.")

    def get_lifespan(self):
        return self.lifespan


class Dog(Animals, Interface):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def eats(self):
        print("A dog eats meat, veggies, dog-food etc.!")

    def color(self):
        print("A dog could be of any color, it depends on the breed.")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A Dog makes " + self.sound + " sound.")

    def typeOfAnimal(self):
        print("Dog is an omnivorous animal")

    def attackHumans(self):
        print("Dogs won't attack any human without a reason. If it senses threat from someone then it attacks it.")

    def is_extinct(self):
        print("No, Dog is not extinct.")

    def get_lifespan(self):
        return self.lifespan

class Rat(Animals, Interface):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def eats(self):
        print("LRat eats flesh, leftover food, garbage etc.!")

    def color(self):
        print("Rats can be white, black or gray in color!")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A Rat makes " + self.sound + " sound.")

    def typeOfAnimal(self):
        print("Rat is an omnivorous animal")

    def attackHumans(self):
        print("Rats are of no harm to humans.")

    def is_extinct(self):
        print("No, Rat is not extinct.")

    def get_lifespan(self):
        return self.lifespan

class Kangaroo(Animals, Interface):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def eats(self):
        print("A Kangaroo eats vegetables, plants, leaves!")

    def color(self):
        print("A Kangaroo is blue-grey or brown in color!")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A Kangaroo makes " + self.sound + " sound.")

    def attackHumans(self):
        print("A Kangaroo may punch you in the face so stay away from them :)")

    def is_extinct(self):
        print("No, Kangaroo is not extinct.")

    def get_lifespan(self):
        return self.lifespan


class PolarBear(Animals, Interface):

    def __init__(self, lifespan):
        Animals.__init__(self)
        self.lifespan = lifespan

    def eats(self):
        print("Polar Bear eats meat!")

    def color(self):
        print("Color of Polar Bear is off white or bright white.")

    def setsound(self, sound):
        self.sound = sound

    def getsound(self):
        print("A polar bear makes " + self.sound + " sound.")

    def typeOfAnimal(self):
        print("Polar Bear is a carnivorous animal")

    def attackHumans(self):
        print("A Polar Bear may attack humans if hungry.")

    def is_extinct(self):
        print("No, PolarBear is not extinct.")

    def get_lifespan(self):
        return self.lifespan
        
        

lion = Lion('20 years')
lion.setsound('Roaring')
lion.typeOfAnimal()
print(lion.getsound())
print(lion.is_living)
lion.eats()
print(lion.get_lifespan())
print('\n')

saber = SaberTooth('30 years')
saber.is_extinct()
saber.eats()
print(saber.legs)








