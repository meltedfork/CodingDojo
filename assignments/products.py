class Products(object):
    def __init__(self, price, item, weight, brand, status = 'for sale'):
        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.status = status
        self.displayInfo()

    def sell(self):
        if self.status is sold:
            print 'sold'
        elif self.status is sale:
            print 'for sale' 
        else:
            giveback(self)      
        return self

    def salesTax(self, tax):
        sales = self.price * (1 + tax)
        return sales

    def giveBack(self, reason):
        if self.status is defect:
            print 'defective'
            self.price == 0
        if self.status is opened:  
            print 'like new'
            self.status == 'for sale'
        if self.status is used:    
            print 'used'
            self.status == 'used'
            self.price == self.price * .80
        return self

    def displayInfo(self):    
        print 'Does this work?', self.price, self.item, self.weight, self.brand, self.status 
        return self


prod1 = Products(3.00, 'lettuce', 0.5, 'Farm Fresh').salesTax(.095)

        
        
        