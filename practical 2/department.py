class Department:
    def __init__(self, name):
        if not name.strip():
            raise ValueError("Department name cannot be blank")
        self.name = name

    def summary(self):
        # Extension 2: department summary method
        return f"Department: {self.name}"

    def __str__(self):
        return self.name