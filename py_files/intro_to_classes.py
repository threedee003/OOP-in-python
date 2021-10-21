"""
Author : Tribikram Dhar
Date : 21.10.2021
A basic class with a method to calculate prices of products

"""


class Item:
    def calculate_total_price(self, x, y):
        return x*y





item1 = Item()
item1.name = "Iphone11"
item1.price = 50000
item1.quantity = 5
print(item1.calculate_total_price(item1.price,item1.quantity))


item2 = Item()
item2.name = "Hp pavillion"
item2.price = 70000
item2.quantity = 4
print(item2.calculate_total_price(item2.price,item2.quantity))


