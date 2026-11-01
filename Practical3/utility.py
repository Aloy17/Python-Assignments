def show_menu():
    print("\n=== Utility Calculator ===")
    print("1. Add numbers")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show summary")
    print("6. Average")
    print("0. Exit")


def get_number(prompt="Enter a number: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def add(*args):
    return sum(args)


def avg(*args):
    if not args:
        raise ValueError("At least one number is required.")
    return add(*args) / len(args)


def calculate(a, b, operation="+"):
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

def grade_from_marks(marks, maximum=100):
    if not 0 <= marks <= maximum:
        return "ERROR"
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    return "FAIL"


def show_summary(**kwargs):
    print("\n--- Summary ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def main():
    history = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice not in {"1", "2", "3", "4", "5", "6"}:
            print("Invalid menu choice. Try again.")
            continue

        elif choice == "5":
            show_summary(
                total_calculations=len(history),
                last_result=history[-1] if history else "No calculations yet"
            )
            continue

        if choice == "1":
            a = get_number("First number: ")
            b = get_number("Second number: ")
            result = add(a, b)
            label = "addition"

        elif choice == "2":
            a = get_number("First number: ")
            b = get_number("Second number: ")
            result = calculate(a, b, "-")
            label = "subtraction"

        elif choice == "3":
            a = get_number("First number: ")
            b = get_number("Second number: ")
            result = calculate(a, b, "*")
            label = "multiplication"

        elif choice == "6":
            marks = [
                get_number("First mark: "),
                get_number("Second mark: "),
                get_number("Third mark: "),
            ]
            if any(not 0 <= mark <= 100 for mark in marks):
                print("Marks must be between 0 and 100.")
                continue
            result = avg(*marks)
            grade = grade_from_marks(result)
            label = f"average (Grade {grade})"

        else:
            a = get_number("First number: ")
            b = get_number("Second number: ")
            try:
                result = calculate(a, b, "/")
            except ZeroDivisionError as error:
                print("Error:", error)
                continue

            label = "division"

        print(f"Result ({label}): {result:.2f}")
        history.append(result)

    


if __name__ == "__main__":
    main()