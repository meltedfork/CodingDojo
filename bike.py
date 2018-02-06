print 'ride a bike'

class Bike(object):
    def __init__(self, price, max_speed, miles = 0): 
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print self.price, self.max_speed, self.miles

    def ride(self):
        self.miles = self.miles + 10
        print 'Riding', 'Total miles: ', self.miles

    def reverse(self):
        self.miles = self.miles - 5
        print 'Reversing', 'Total miles: ', self.miles

bike1 = Bike(200, "25 mph")
bike2 = Bike(300, "20 mph")
bike3 = Bike(450, "30 mph")
# print bike1.miles, bike2.miles, bike3.miles
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()