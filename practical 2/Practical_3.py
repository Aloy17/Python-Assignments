def show_menu():
    print("\n=== Utility Calculator ===")
    print("1. Add numbers")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show summary")
    print("0. Exit")


def get_number(prompt="Enter a number: "):
    # keeps asking until a valid float is entered
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def add(*args):
    # accepts any number of positional values
    return sum(args)


def calculate(a, b, operation="+"):
    # default operation is addition
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Unsupported operation.")


def show_summary(**kwargs):
    # collects named values into a dictionary
    print("\n--- Summary ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def average(a, b, c):
    # extension A: reusable average using add
    return add(a, b, c) / 3


def grade_from_marks(marks, maximum=100):
    # extension B: grade bands with range validation
    if marks < 0 or marks > maximum:
        raise ValueError(f"Marks must be between 0 and {maximum}.")
    percentage = (marks / maximum) * 100
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def scope_demo():
    # extension C: local variable inside a function
    local_var = "I am local"
    print("Inside function:", local_var)


def run_extensions():
    # runs all extension tasks once at startup
    print("\n=== Extension Tasks ===")

    print("\nA. Average of 10, 20, 30:", average(10, 20, 30))

    print("\nB. Grade for 85/100:", grade_from_marks(85))
    print("   Grade for 72/80:", grade_from_marks(72, maximum=80))
    try:
        grade_from_marks(120)
    except ValueError as e:
        print("   Validation error:", e)

    print("\nC. Scope demo:")
    scope_demo()
    try:
        print(local_var)
    except NameError as e:
        print("   Outside function:", e)

    print("\nD. add(2, 4, 6, 8) =", add(2, 4, 6, 8))

    print("\nE.", end="")
    show_summary(student="Student A", practical=3, status="Complete")


def main():
    # stores results of each calculation
    history = []
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid menu choice. Try again.")
            continue
        elif choice == "5":
            show_summary(
                total_calculations=len(history),
                last_result=history[-1] if history else "No calculations yet"
            )
            continue

        a = get_number("First number: ")
        b = get_number("Second number: ")

        if choice == "1":
            result = add(a, b)
            label = "addition"
        elif choice == "2":
            result = calculate(a, b, "-")
            label = "subtraction"
        elif choice == "3":
            result = calculate(a, b, "*")
            label = "multiplication"
        else:
            try:
                result = calculate(a, b, "/")
            except ZeroDivisionError as error:
                print("Error:", error)
                continue
            label = "division"

        # lambda formats result to two decimal places
        format_result = lambda value: f"{value:.2f}"
        print(f"Result ({label}): {format_result(result)}")
        history.append(result)


if __name__ == "__main__":
    run_extensions()
    main()