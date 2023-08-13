import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    menu = [
        "1. Check sales statistics by gender",
        "2. Check sales statistics by age",
        "3. Check sales statistics by state",
        "4. Check sales statistics by marital status",
        "5. Check sales statistics by occupation",
        "6. Check sales statistics by product category",
        "0. Exit"
    ]
    screen_width = os.get_terminal_size().columns
    menu_width = max(len(line) for line in menu)
    margin = (screen_width - menu_width) // 2

    print("\n" * (os.get_terminal_size().lines // 3))
    print(" " * margin + "CHOICE MENU")
    print("-" * screen_width)

    for line in menu:
        print(" " * margin + line)

    print("-" * screen_width)

def check_sales_statistics(choice):
    # Add your code to calculate and display sales statistics based on the chosen option
    # You can use if/elif statements to handle different choices

    if choice == '1':
        print("Sales statistics by gender")
    elif choice == '2':
        print("Sales statistics by age")
    elif choice == '3':
        print("Sales statistics by state")
    elif choice == '4':
        print("Sales statistics by marital status")
    elif choice == '5':
        print("Sales statistics by occupation")
    elif choice == '6':
        print("Sales statistics by product category")

    # Wait for user to press Enter before returning to the menu
    input("\nPress Enter to continue...")
    show_menu()

def show_menu():
    print_menu()
    choice = int(input("Enter your choice (0-6): "))
    while choice not in [0, 1, 2, 3,4,5,6]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (0-6): ")

    if choice == 0:
        clear_screen()
        print("Goodbye!")
    else:
        return choice

