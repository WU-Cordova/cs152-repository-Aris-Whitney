BEARCAT BISTRO ORDERING SYSTEM- README

Overview of project:
    This ordering system is designed to help with the management of customer orders at the bistro.

    It offers:
        1. Access to the bitro menu (Couldn't get access to the links provided in the assignment so i had to look at a picutre of the menu online so names and prices may be outdated)

        2.ability to take orders and customize them

        3.Access to open orders 
        
        4.marking orders as complete

        5. an end-of-day report recording total sales and drink details

        6.A way to exit the system


DATA STRUCTURE CHOICES:

    Menu:
        Data structure used: Array
            Why?: Menu contains a list of 5 fixed drinks that do not change, and since Array allows indexed access in time O(1) it prevents the list size from changing
            
            Tradeoffs: won't be ideal for adding or removing items from the menu

    Customer Order:
        Data structure used:Linked List
            Why?: The linked list allows the customers to make more than one order, providing O(1) which helps for adding drinks. List doesn;t need to be resized

            tradeoffs: extra memory to store refernces to the item next in the list

    Order Confirmation:
        Data Structure:Linked List
            Why?: When drinks are added to the order it can handle it more efficiently to maintain the order of the drinks. It is also traversal meaning that it retireves the information in order. With a time complexity of O(n), with n being the number of drinks in the order

        Tradeoffs: it makes looking things up slower compared to using arrays





    Open Orders:
        Data Structure:List Stack
            Why?:It follows Last in First out meaning that the most recent orders will pop up first. Has O(1) push and pop operations which makes it better for processing orders as they are being turned in and finished

            tradeoffs: stacks aren't ideal for First in first out processing, a deque would be better for FIFO operations

    Completed Orders:
        Data Structure:Linked List
            Why?:Completed orders are stored in a linked list and this allows for more complex additions when creating the end of day report. Can easliy append and remove orders

            tradeoffs: Like mentioned before, it has extra memory


    Instructions for running the program:

        If you copy my repository and go to Project 3 folder and click the program.py file-hit run in terminal it should give you 6 options to choose from to start the ordering system.



    Bugs/ Limitations:

        This code doesn't allow you to order more than one of the same drink in one order, you have to keep add another order and repeat the process.

        The Data isn't saved when you exit the program

        It doesn't auto correct spelling, and if you mispell for ex. Latte as Late it will say it is invalid


    Future Enhancements:

        I think it would be cool to add an option to tip the barista.

        I would try implementing Deque so that it follows FIFO so the orders that are there the longest are processed first

        It would also be useful to add the total amount the customer owes

SAMPLE RUN:

--- Bearcat Bistro ---
1. Display Menu
2. Take New Order
3.View open orders
4. Mark next order as complete
5.View end-of-day report
6.Exit
Please select an option (1-6): 1

--- Bearcat Bistro Menu ---
Americano - $2.50
Espresso - $2.50
Latte - $3.75
Mocha - $4.20
Jamocha - $3.75

--- Bearcat Bistro ---
1. Display Menu
2. Take New Order
3.View open orders
4. Mark next order as complete
5.View end-of-day report
6.Exit
Please select an option (1-6): 2
Enter the customer's name: Aris

--- Bearcat Bistro Menu ---
Americano - $2.50
Espresso - $2.50
Latte - $3.75
Mocha - $4.20
Jamocha - $3.75
Enter the name of the drink from the menu: Espresso
Enter customization for Espresso (or press enter to skip this step): extra shot
Do you want to order another drink? (yes/no): yes

--- Bearcat Bistro Menu ---
Americano - $2.50
Espresso - $2.50
Latte - $3.75
Mocha - $4.20
Jamocha - $3.75
Enter the name of the drink from the menu: Jamocha
Enter customization for Jamocha (or press enter to skip this step):             
Do you want to order another drink? (yes/no): no
Order confirmed for Aris.
order for Aris: Espresso (extra shot),Jamocha (No Customization)

--- Bearcat Bistro ---
1. Display Menu
2. Take New Order
3.View open orders
4. Mark next order as complete
5.View end-of-day report
6.Exit
Please select an option (1-6): 3

 --- OPEN ORDERS ---
order for Aris: Espresso (extra shot),Jamocha (No Customization)

--- Bearcat Bistro ---
1. Display Menu
2. Take New Order
3.View open orders
4. Mark next order as complete
5.View end-of-day report
6.Exit
Please select an option (1-6): 4
Order for Aris is complete.

--- Bearcat Bistro ---
1. Display Menu
2. Take New Order
3.View open orders
4. Mark next order as complete
5.View end-of-day report
6.Exit
Please select an option (1-6): 5

 --- END-OF-DAY-REPORT ---
Total Revenue: $6.25
Total Drinks Sold: 2
Americano:Sold 0 times, Total Sales: $0.00
Espresso:Sold 1 times, Total Sales: $2.50
Latte:Sold 0 times, Total Sales: $0.00
Mocha:Sold 0 times, Total Sales: $0.00
Jamocha:Sold 1 times, Total Sales: $3.75

--- Bearcat Bistro ---
1. Display Menu
2. Take New Order
3.View open orders
4. Mark next order as complete
5.View end-of-day report
6.Exit
Please select an option (1-6): 6
Thank you for using the Bearcat Bistro system. Have a good day!