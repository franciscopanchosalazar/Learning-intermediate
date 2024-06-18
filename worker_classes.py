class Staff:
    raise_amount = 0

    def __init__(self, name: str, surname: str, department: str, salary: float):
        self.rate = None
        self.name = name.lower()
        self.surname = surname.lower()
        self.department = department.lower()
        self.salary = float(salary)
        self.email = f"{self.name}_{surname}@{self.department}company.com"

    def salary_rate(self):
        self.rate = self.salary * self.raise_amount
        self.salary = self.salary + self.rate

    def worker_profile(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary}")


class Electricians(Staff):  # Classes inheritance
    raise_amount = 0.2

    def __init__(self, name: str, surname: str, department: str, salary: float, experience: int):
        super().__init__(name, surname, department, salary)
        self.experience = experience


worker_one = Electricians("pancho", "Salazar", "maintenance", 580, 3)
print(f"{worker_one.experience} Years")

worker_one.worker_profile()
