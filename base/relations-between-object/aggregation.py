class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return int(((self.pay * 10) + self.bonus) / 0.07)


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age

        self.agg_salary = salary

    def total_salary(self):
        return self.agg_salary.annual_salary()


salary = Salary(1000, 1500)

employee = Employee('amir', 23, salary)

print(employee.total_salary())
