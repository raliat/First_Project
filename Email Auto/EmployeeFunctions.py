from EmployeeGroups import Employee_group
from Employees import Employee 

def list_all_employees():
    for employee in Employee.employee_list:
        print (employee.name,employee.email,employee.user_ID)

def list_all_groups():
    for group in Employee_group.employee_groups:
        print(group.name)