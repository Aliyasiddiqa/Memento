def greet(name):
    print(f"Hello, {name}! Welcome to your Memento project.")
    with open("visitors.txt", "a") as file:
        file.write(name + "\n")

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Get greeted")
    print("2. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        user_name = input("What's your name? ")
        greet(user_name)
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Please enter 1 or 2.")