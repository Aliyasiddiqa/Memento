def greet(name):
    print(f"Hello, {name}! Welcome to your Memento project.")
    with open("visitors.txt", "a") as file:
        file.write(name + "\n")

def show_visitors():
    print("\nVisitors so far:")
    try:
        with open("visitors.txt", "r") as file:
            visitors = file.readlines()
            for visitor in visitors:
                print(visitor.strip())
    except FileNotFoundError:
        print("No visitors yet!")

def clear_visitors():
    open("visitors.txt", "w").close()
    print("Visitor list cleared!")

def count_visitors():
    try:
        with open("visitors.txt", "r") as file:
            visitors = file.readlines()
            print(f"\nTotal visitors: {len(visitors)}")
    except FileNotFoundError:
        print("\nTotal visitors: 0")

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Get greeted")
    print("2. Show all visitors")
    print("3. Clear visitor list")
    print("4. Show visitor count")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1, 2, 3, 4 or 5): ")
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
        print("Goodbye!")
        break
    else:
        print("Please enter 1, 2, 3, 4 or 5.")