"""
Author : T.Dhar
Date : 21.10.2021
"""


class Item:
    pay_rate = 0.9                                                                                #percentage of price after discount
    def __init__(self, name : str, price : float, quantity : int):
        assert price >= 0 , f"Price {price} is not greater than zero"                              # makes sure if the value is greater than zero
        assert quantity >= 0 , f"Quantity {quantity} is not greater than zero"
        self.name = name                       #attributes :  name,price,quantity
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price*self.quantity






item1 = Item("Iphone11",50000,5)     #instances
item2 = Item("Hp pavillion",70000,4)

#item2.has_gpu = True

print(item1.calculate_total_price())
print(item2.calculate_total_price())

print(Item.__dict__)                       # prints all attributes in class level
print(item1.__dict__)                      # prints all attributes in instance level






