from staff_app import Department, Developer, Manager


def main():
    engineering = Department("Engineering")
    dev = Developer("Riya", "EMP101", engineering, "Python")
    dev.salary = 65000
    print(dev.describe())
    print("Salary:", dev.salary)

    # Extension 3: invalid salary
    try:
        dev.salary = -100
    except ValueError as error:
        print("Validation:", error)

    # Extension 3: blank name
    try:
        Developer("   ", "EMP102", engineering, "Go")
    except ValueError as error:
        print("Validation:", error)

    # Extension 1 + 2 demo
    manager = Manager("Arjun", "EMP200", engineering, 5)
    manager.salary = 80000
    print(manager.describe())
    print(engineering.summary())

    # HAS-A inspection
    print("dev.department is Department object:", isinstance(dev.department, Department))

    # IS-A inspection
    from staff_app import Employee, Person
    print("Developer IS-A Employee:", issubclass(Developer, Employee))
    print("Developer IS-A Person:  ", issubclass(Developer, Person))


if __name__ == "__main__":
    main()