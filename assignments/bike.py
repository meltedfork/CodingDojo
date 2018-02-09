print 'ride a bike'

class Bike(object):
    def __init__(self, price, max_speed, miles = 0): 
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self

    def ride(self):
        self.miles = self.miles + 10
        #print 'Riding', 'Total miles: ', self.miles
        return self

    def reverse(self):
        self.miles = self.miles - 5
        #print 'Reversing', 'Total miles: ', self.miles
        return self

bike1 = Bike(200, "25 mph")
bike2 = Bike(300, "20 mph")
bike3 = Bike(450, "30 mph")
# print bike1.miles, bike2.miles, bike3.miles
bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
