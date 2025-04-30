import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from datastructures.array import Array
from datastructures.deque import Deque
from datastructures.liststack import ListStack
from datastructures.linkedlist import LinkedList
from drink import Drink
from order_item import OrderItem
from customer_order import CustomerOrder

class BistroSystem:
    def __init__(self):
        self.menu=Array([Drink("Americano", 2.50), Drink("Espresso", 2.50), Drink("Latte", 3.75), Drink("Mocha", 4.20), Drink("Jamocha", 3.75)]) #Creates an array of drink options with pricing
        self.open_orders=ListStack(CustomerOrder) #Will list the active customer orders
        self.completed_orders=LinkedList[CustomerOrder]() #Will list the orders that have been completed
        self.sales_data={drink.name:0 for drink in self.menu} #Will record what drinks were purchased

    def display_menu(self):
        print("\n--- Bearcat Bistro Menu ---") #Dispplays the drink menu with drink names and price
        for drink in self.menu:
            print(drink)

    def take_order(self):
        customer_name=input("Enter the customer's name: ") #Asks for user input for custumer name
        order=CustomerOrder(customer_name) #returns the name of the customer and their corresponding order

        while True:
            self.display_menu() #Shows customer the menu options
            drink_name=input("Enter the name of the drink from the menu: ") #asks for user input to get single drink order
            drink=next((d for d in self.menu if d.name.lower() == drink_name.lower()), None) #doesn't make answer case sensitive

            if drink:
                customization=input(f"Enter customization for {drink.name} (or press enter to skip this step): ") #asks for user input for modifications
                order.add_item(OrderItem(drink, customization)) #adds completed order with customization notes
                self.sales_data[drink.name] +=1 #adds that 1 drink to end of day sales report
            else:
                print("Invalid drink name. Please choose from the given menu.") #If user inputs name that doesn't match drink names provided, pops up an error and asks if they again what drink they want

            another=input("Do you want to order another drink? (yes/no): ").strip().lower() #asks customer if they want to add another drink to their order
            if another != 'yes': #if they say no, finish processing order
                break
        print(f"Order confirmed for {customer_name}.") #confirm order with customer name
        print(order)
        self.open_orders.push(order) #pushes order to the front of open orders

    def view_open_orders(self): #shows open orders
        if self.open_orders.empty: #if there are currently no open orders says "No Open Orders"
            print("No open orders.")
        else:
            print("\n --- OPEN ORDERS ---")#othherwise it prints order with customer names and order details
            for order in self.open_orders:
                print(order)

    def mark_next_order_complete(self): #Marks available order complete, untherwise says there are no orders to complete
        if self.open_orders.empty:
            print("NO ORDERS TO COMPLETE.")
        else:
            completed_order=self.open_orders.pop()
            self.completed_orders.append(completed_order)
            print(f"Order for {completed_order.customer_name} is complete.")

    def end_of_day_report(self): #shows individual sales of drink types and how much money that drink made, also shows total revenue and total number of drinks sold
        print("\n --- END-OF-DAY-REPORT ---")
        total_sales=sum(drink.price * count for drink, count in zip(self.menu, self.sales_data.values()))
        print(f"Total Revenue: ${total_sales:.2f}")
        print(f"Total Drinks Sold: {sum(self.sales_data.values())}")

        for drink in self.menu:
            drink_sales=self.sales_data[drink.name]
            print(f"{drink.name}:Sold {drink_sales} times, Total Sales: ${drink_sales*drink.price:.2f}")

    def exit_system(self): #exits the bistro system
        print("Thank you for using the Bearcat Bistro system. Have a good day!")
