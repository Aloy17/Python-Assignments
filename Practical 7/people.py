from .department import Department


class Person:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("Name cannot be blank")
        self.name = name

    def describe(self):
        return f"Person: {self.name}"


class Employee(Person):
    def __init__(self, name, employee_id, department):
        super().__init__(name)
        self.employee_id = employee_id
        if not isinstance(department, Department):
            raise TypeError("department must be a Department object")
        self.department = department
        self._salary = 0.0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if amount < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = float(amount)

    def describe(self):
        return (f"Employee: {self.name}, ID: {self.employee_id}, "
                f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, employee_id, department, language):
        super().__init__(name, employee_id, department)
        self.language = language

    def describe(self):
        return (f"{super().describe()}, "
                f"Role: Developer, Language: {self.language}")


class Manager(Employee):
    # Extension 1: Manager subclass with team_size property
    def __init__(self, name, employee_id, department, team_size):
        super().__init__(name, employee_id, department)
        self.team_size = team_size

    @property
    def team_size(self):
        return self._team_size

    @team_size.setter
    def team_size(self, value):
        if value < 0:
            raise ValueError("Team size cannot be negative")
        self._team_size = int(value)

    def describe(self):
        return (f"{super().describe()}, "
                f"Role: Manager, Team size: {self.team_size}")