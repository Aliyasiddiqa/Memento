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

def search_visitor():
    name_to_search = input("Enter the name to search: ")
    found = False
    try:
        with open("visitors.txt", "r") as file:
            visitors = file.readlines()
            for visitor in visitors:
                if visitor.strip().lower() == name_to_search.lower():
                    found = True
                    break
        if found:
            print(f"{name_to_search} is in the visitor list!")
        else:
            print(f"{name_to_search} is NOT in the visitor list.")
    except FileNotFoundError:
        print("No visitors yet!")

def export_visitors():
    try:
        with open("visitors.txt", "r") as infile, open("exported_visitors.txt", "w") as outfile:
            visitors = infile.readlines()
            outfile.writelines(visitors)
        print("Visitors exported to exported_visitors.txt!")
    except FileNotFoundError:
        print("No visitors to export!")

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Get greeted")
    print("2. Show all visitors")
    print("3. Clear visitor list")
    print("4. Show visitor count")
    print("5. Search for a visitor")
    print("6. Export visitors")
    print("7. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1, 2, 3, 4, 5, 6 or 7): ")
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
    else:
        print("Please enter 1, 2, 3, 4, 5, 6 or 7.")