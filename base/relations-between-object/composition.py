class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return int(((self.pay * 10) + self.bonus) * 0.07)


class Employee:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age

        self.obj_salary = Salary(pay, bonus)

    def total_salary(self):
        return self.obj_salary.annual_salary()


employee = Employee('amir', 23, 1000, 1500)
print(employee.total_salary())
