# Part A / B: recursive factorial
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case


# Part B: recursive linear search
def recursive_search(items, target, index=0):
    if index >= len(items):       # base case: end reached
        return -1
    if items[index] == target:
        return index
    return recursive_search(items, target, index + 1)


# Part C: custom exception for application rules
class InvalidInputError(Exception):
    pass


def read_non_negative_integer():
    raw = input("Enter a non-negative integer: ")
    try:
        value = int(raw)
        if value < 0:
            raise InvalidInputError("Number cannot be negative.")
    except ValueError:
        print("Input error: enter a whole number, such as 4.")
        return None
    except InvalidInputError as error:
        print(f"Validation error: {error}")
        return None
    else:
        print("Input accepted.")
        return value
    finally:
        print("Input validation attempt finished.")


# Part D: seeded bug (kept for reference and demonstration)
def factorial_buggy(n):
    if n == 0:
        return 0                  # BUG: should be 1
    return n * factorial_buggy(n - 1)


# Part D: corrected version
def factorial_fixed(n):
    if n == 0:
        return 1                  # FIXED: 0! equals 1
    return n * factorial_fixed(n - 1)


def run_tests():
    print("=== Recursive factorial ===")
    print("factorial(0) =", factorial(0))
    print("factorial(1) =", factorial(1))
    print("factorial(5) =", factorial(5))
    try:
        factorial(-2)
    except ValueError as e:
        print("factorial(-2) raised ValueError:", e)

    print("\n=== Recursive search ===")
    print("search([8, 3, 12], 8)  =", recursive_search([8, 3, 12], 8))
    print("search([8, 3, 12], 12) =", recursive_search([8, 3, 12], 12))
    print("search([8, 3, 12], 5)  =", recursive_search([8, 3, 12], 5))

    print("\n=== Seeded bug vs fixed ===")
    print("factorial_buggy(4) =", factorial_buggy(4))
    print("factorial_fixed(0) =", factorial_fixed(0))
    print("factorial_fixed(4) =", factorial_fixed(4))


def main():
    run_tests()
    print("\n=== Interactive validation ===")
    number = read_non_negative_integer()
    if number is not None:
        print("Factorial:", factorial(number))


if __name__ == "__main__":
    main()