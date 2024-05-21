from abc import ABC, abstractmethod

class Employee:

    def __init__(self, name, employee_id, position, salary):
        self._name = None
        self._employee_id = None
        self._position = None
        self._salary = salary

    def __str__(self):
        return (f'Имя {self._name}\n'
                f'Ай ди {self._employee_id}\n'
                f'Позиция {self._position}\n'
                f'Salary {self._salary}')

class Builder(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def set_name(self, name):
        ...

    @abstractmethod
    def set_employee_id(self, employee_id):
        ...

    @abstractmethod
    def set_position(self, position):
        ...

    @abstractmethod
    def set_salary(self, salary):
        ...

    @abstractmethod
    def get_employee(self):
        ...


class EmployeeBuilder(Builder):
    _employee: Employee

    def create(self):
        self._employee = Employee()

    def set_name(self, name):
        self._employee.name = name

    def set_employee_id(self, employee_id):
        self._employee.set_employee_id = employee_id

    def set_position(self, position):
        self._employee.position = position

    def set_salary(self, salary):
        self._employee.salary = salary

    def get_employee(self):
        return self._employee

class Institute:

    def __init__(self, employee: Employee):
        self.__employee = employee

    def make(self, name, employee_id, position, salary):
        self.__employee.name = name
        self.__employee.employee_id = employee_id
        self.__employee.position = position
        self.__employee.salary = salary
        return self.__employee.get_employee


employee = EmployeeBuilder()
EmployeeBuilder.create()
EmployeeBuilder.set_name('peps')
EmployeeBuilder.set_employee_id(234)
print(employee)


