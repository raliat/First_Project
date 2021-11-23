class Employee_group:
    employee_groups = []
    def __init__(self, name):
        self._name = name 
        self._list_of_employees = []
        Employee_group.employee_groups.append(self)
    
    def add_employee(self, employee):
        self._list_of_employees.append(employee)

    def __repr__(self) -> str:
        return f'Employee_group({self._name})'

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name = value

    @property
    def list_of_employees(self):
        return self._list_of_employees