# PLP Python Week 8 - My Python Toolkit

# Tool 1: Number Guessing Game
# The user keeps guessing until they find the secret number.
def guessing_game():
    secret_number = 9
    guess = 20

    print("\nWelcome to the Number Guessing Game!")
    print("Guess a number between 1 and 10.")

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed {secret_number} correctly!")

        except ValueError:
            print("Please enter a valid whole number.")


# Tool 2: To-Do List
# The user can add, view, and remove tasks from a list.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter your task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully!")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

                try:
                    task_number = int(input("Enter task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Task '{removed}' removed successfully!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Returning to the main menu...")
            break

        else:
            print("Invalid choice. Please choose between 1 and 4.")


# Tool 3: Simple Calculator
# The user can perform basic mathematical calculations.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Choose an operation (1-4): ")

        if operation == "1":
            result = num1 + num2
            print(f"The sum is: {result}")

        elif operation == "2":
            result = num1 - num2
            print(f"The difference is: {result}")

        elif operation == "3":
            result = num1 * num2
            print(f"The product is: {result}")

        elif operation == "4":
            if num2 == 0:
                print("Sorry, you cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The division result is: {result}")

        else:
            print("Invalid operation.")

    except ValueError:
        print("Please enter valid numbers.")


# Main program: Displays the menu and runs the selected tool.
def main():
    print("Welcome to My Python Toolkit!")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Number Guessing Game")
        print("2. To-Do List")
        print("3. Simple Calculator")
        print("4. Quit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            guessing_game()

        elif choice == "2":
            todo_list()

        elif choice == "3":
            calculator()

        elif choice == "4":
            print("Thank you for using My Python Toolkit. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")


# Start the program
if __name__ == "__main__":
    main()