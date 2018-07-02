class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self 
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print (self.health)
        return self

animal1 = Animal("Nem", 500)

animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog,self).__init__(name,150)
    def pet():
        self.health += 5
        return self

my_nem = Dog("Nem")

my_nem.walk().walk().walk().run().run().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon,self).__init__(name, 170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print ("I'm a Dragon")
        super(Dragon,self).display_health()

my_dragon = Dragon("Inferno")

animal2 = Animal("Noa", 400)
animal2.pet()
animal2.fly()
animal2.display_health()
        