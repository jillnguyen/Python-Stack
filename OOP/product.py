class Product(object):
        def __init__(self, price, item_name, weight, brand):
            self.price = price
            self.item_name = item_name
            self.weight = weight
            self.brand = brand
            self.status = "for sale"
        def sell(self):
            self.status = "sold"
            return self
        def add_tax(self, rate):
            self.price = self.price * (1 + rate)
            return self 
        def refund(self, reason):
            if reason == "defective":
                self.status = "defective"
                self.price = 0
            elif reason == "new":
                self.status = "for sale"
            elif reason == "opened":
                self.status = "used"
                self.price *= 0.8
            return self
        def display_info(self):
            print(self.price, self.item_name, self.weight, self.brand, self.status)
            return self

product1 = Product(500, "laptop", 20, "Lenovo")
product1.sell().add_tax(0.15).refund("opened").display_info()