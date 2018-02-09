class Animal(object):
    
    def __init__(self, name):
        self.name = name
        self.health = 100
       
    def walk(self):
        self.health -= 1
        return self  

    def run(self):
        self.health -= 5
        return self
        

    def displayHealth(self):
        print self.name, 'Health is:', self.health
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5            
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170  

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print 'I am a dragon!'        

animal1 = Animal('Parrot')
animal1.walk().walk().walk().run().run().displayHealth()
animal2 = Dog('Dawg')
animal2.walk().walk().walk().run().run().pet().displayHealth()
animal3 = Dragon('Scorch')
animal3.fly().fly().displayHealth()
