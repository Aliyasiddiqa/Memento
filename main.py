def welcome():
    print("************************************")
    print(" Welcome to the Memento Visitor App ")
    print("************************************")

def show_help():
    print("\nHelp Menu:")
    print("1. Get greeted - Enter your name to be greeted and added to the visitor list.")
    print("2. Show all visitors - See everyone who has been greeted.")
    print("3. Clear visitor list - Remove all names from the visitor list.")
    print("4. Show visitor count - See how many visitors there are.")
    print("5. Search for a visitor - Find out if a name is in the visitor list.")
    print("6. Export visitors - Save all visitors to a new file.")
    print("7. Exit - Close the program.")
    print("8. Help - Show this help menu.")

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Get greeted")
    print("2. Show all visitors")
    print("3. Clear visitor list")
    print("4. Show visitor count")
    print("5. Search for a visitor")
    print("6. Export visitors")
    print("7. Exit")
    print("8. Help")

welcome()  # Show welcome message when program starts

while True:
    show_menu()
    choice = input("Enter your choice (1-8): ")
    if choice == "1":
        user_name = input("What's your name? ")
        greet(user_name)
    elif choice == "2":
        show_visitors()
    elif choice == "3":
        clear_visitors()
    elif choice == "4":
        count_visitors()
    elif choice == "5":
        search_visitor()
    elif choice == "6":
        export_visitors()
    elif choice == "7":
        print("Goodbye!")
        break
    elif choice == "8":
        show_help()
    else:
        print("Please enter a number from 1 to 8.")