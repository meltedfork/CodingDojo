class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.displayAll()    
        
    def displayAll(self):
        print 'Price: $', self.price 
        print 'Speed:', self.speed 
        print 'Fuel:', self.fuel 
        print 'Mileage:', self.mileage 
        print 'Tax:', self.tax  
        return self
        
car1 = Car(2000, '35 mph', 'Full', '15 mpg')
car2 = Car(50000, '75 mph', 'Half', '28 mpg')
