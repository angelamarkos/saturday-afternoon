import os
import csv
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name, title, level):
        self.id = employee_id
        self.name = name
        self.title = title
        self.level = level

    @abstractmethod
    def calculate_pay(self):
        pass

    def __repr__(self):
        return f'{self.name} - {self.title} - {self.level}'

class Bonus(ABC):
    def __init__(self, sales, percent):
        self.bonus = sales * percent / 100


class SalaryEmployee(Employee):
    def __init__(self, employee_id, name, title, level, salary):
        super().__init__(employee_id, name, title, level)
        if salary.isdigit():
            self.salary = int(salary)
        else:
            raise Exception('Wrong type.')

    def calculate_pay(self):
        return self.salary

class HourlyEmployee(Employee):
    def __init__(self, employee_id, name, title, level, salary, hours_worked):
        super().__init__(employee_id, name, title, level)
        self.hourly_rate = int(salary)
        self.hours_worked = int(hours_worked)

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

class BonusSalaryEmployee(SalaryEmployee, Bonus):
    def __init__(self, employee_id, name, title, level, salary, sales, percent):
        SalaryEmployee.__init__(self, employee_id, name, title, level, salary)
        Bonus.__init__(self, sales, percent)

    def calculate_pay(self):
        return super().calculate_pay() + self.bonus

class BonusHourlyEmployee(HourlyEmployee, Bonus):
    def __init__(self, employee_id, name, title, level, salary, hours_worked, sales, percent):
        HourlyEmployee.__init__(self, employee_id, name, title, level, salary, hours_worked)
        Bonus.__init__(self, sales, percent)

    def calculate_pay(self):
        return HourlyEmployee.calculate_pay(self) + self.bonus


class FactoryEmployee:
    CLASS_MAPPING = {
        'salary': SalaryEmployee,
        'hourly': HourlyEmployee,
        'bonus_salary': BonusSalaryEmployee,
        'bonus_hourly': BonusHourlyEmployee
    }

    @staticmethod
    def get_employee(employee_type='salary', field_mapping=None, **line):
        EmployeeClass = FactoryEmployee.CLASS_MAPPING[employee_type]
        kwargs = {}
        for k, v in line.items():
            if field_mapping:
                k = field_mapping[k]
            if k in EmployeeClass.__init__.__code__.co_varnames:
                kwargs[k] = v
        return EmployeeClass(**kwargs)

    @staticmethod
    def get_employee_type(line):
        if line.get('hourly') == 'Yes':
            employee_type = 'hourly'
        else:
            employee_type = 'salary'

        if line.get('commision_sales'):
            employee_type = f'bonus_{employee_type}'

        return employee_type


    @classmethod
    def get_employees(cls, csv_path, field_mapping=None):
        with open(csv_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                yield FactoryEmployee.get_employee(FactoryEmployee.get_employee_type(line), field_mapping, **line)

csv_path = os.path.normpath('./employee_data.csv')
# emp1 = FactoryEmployee.get_employee(1, 'Ben Johnson', 'Software Engineer', 'Intern', 2000, employee_type='salary')
# emp2 = FactoryEmployee.get_employee(2, 'Alice Jackson__init__.__code__.co_varnames', 'Software Engineer', 'Junior', 40, 23, employee_type='hourly')
# emp3 = FactoryEmployee.get_employee(3, 'Ben Johnson', 'Sales', 'Junior', 5000, 30000, 9, employee_type='bonus_salary')
# emp4 = FactoryEmployee.get_employee(4, 'Ben Johnson', 'Sales', 'Junior', 50, 20, 40000, 9, employee_type='bonus_hourly')

field_mapping = {
    "id": "employee_id",
    "full_name": "name",
    "title": "title",
    "seniority": "level",
    "hourly": "hourly",
    "hours_worked": "hours_worked",
    "salary": "salary",
    "sales": "sales",
    "percent": "percent"
}

employees = FactoryEmployee.get_employees(csv_path, field_mapping)
for employee in employees:
    print(employee, employee.calculate_pay())


