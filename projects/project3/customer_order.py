from order_item import OrderItem
from datastructures.linkedlist import LinkedList

class CustomerOrder:
    def __init__(self, customer_name:str):
        self.customer_name=customer_name
        self.items=LinkedList[OrderItem]() #Uses a list to access all the items that they can order

    def add_item(self, item:OrderItem): #asks customer if they want to add a drink
        self.items.append(item)

    def __repr__(self):
        return f"order for {self.customer_name}: {','.join(str(item) for item in self.items)}" #returns customer namen and their drink(s) ordered