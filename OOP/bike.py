class Bike(object):
    def __init__(self,price,max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print (self.price, self.max_speed, self.miles)
        return self
    def ride(self):
        self.miles += 10
        print ("Riding")
        return self
    def reverse(self):
        print("Reversing")
        self.miles -= 5
        return self


bike1 = Bike(500, 100, 200)
bike2 = Bike(1000, 300, 0)
bike3 = Bike(200, 50, 20)

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()



