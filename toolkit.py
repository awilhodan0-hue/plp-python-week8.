# Personal Mini-Toolkit

print("Welcome to My Personal Mini-Toolkit!")

tasks = []

while True:
    print("\n===== MY MINI-TOOLKIT =====")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Checker")
    print("4. Quit")

    choice = input("Enter your choice: ")

    # Tool 1: Simple Calculator
    if choice == "1":
        print("\nSimple Calculator")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose +, -, *, or /: ")

        if operation == "+":
            print(f"Result: {num1 + num2}")
        elif operation == "-":
            print(f"Result: {num1 - num2}")
        elif operation == "*":
            print(f"Result: {num1 * num2}")
        elif operation == "/":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Cannot divide by zero.")
        else:
            print("Invalid operation.")

    # Tool 2: To-Do List
    elif choice == "2":
        while True:
            print("\nTo-Do List")
            print("1. Add task")
            print("2. View tasks")
            print("3. Back to main menu")

            task_choice = input("Choose an option: ")

            if task_choice == "1":
                task = input("Enter your task: ")
                tasks.append(task)
                print(f"Task '{task}' added successfully!")

            elif task_choice == "2":
                if tasks:
                    for number, task in enumerate(tasks, 1):
                        print(f"{number}. {task}")
                else:
                    print("Your task list is empty.")

            elif task_choice == "3":
                break

            else:
                print("Invalid choice. Please try again.")

    # Tool 3: Number Checker
    elif choice == "3":
        number = float(input("Enter a number: "))

        if number > 0:
            print(f"{number} is positive.")
        elif number < 0:
            print(f"{number} is negative.")
        else:
            print("The number is zero.")

    # Quit the program
    elif choice == "4":
        print("Thank you for using my toolkit. Goodbye!")
        break

    else:
        print("Sorry, invalid choice. Please choose 1, 2, 3, or 4.")
