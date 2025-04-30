from bistro_system import BistroSystem

def main():
    bistro_system=BistroSystem()
    menu=["1. Display Menu", "2. Take New Order", "3.View open orders", "4. Mark next order as complete", "5.View end-of-day report", "6.Exit"]
    while True:
        #these shows menu options
        print("\n--- Bearcat Bistro ---")
        print("\n".join(menu))

        #asks for user input
        choice=input("Please select an option (1-6): ")

        #These takes care of the menu options

        if choice =='1':
            bistro_system.display_menu()
        elif choice =='2':
            bistro_system.take_order()
        elif choice =='3':
            bistro_system.view_open_orders()
        elif choice == '4':
            bistro_system.mark_next_order_complete()
        elif choice == '5':
            bistro_system.end_of_day_report()
        elif choice == '6':
            bistro_system.exit_system()
            break
        else:
            print("Invalid choice. Please enter anumber betweem 1 and 6.")

if __name__=="__main__":
    main()