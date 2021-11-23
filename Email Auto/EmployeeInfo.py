# %%
from Employees import Employee
from EmployeeGroups import Employee_group
import EmailFunction
from EmployeeFunctions import list_all_employees, list_all_groups 


emp1 = Employee(name='Robert',user_ID=1,email='crowder2013@gmail.com')
emp2 = Employee(name='Raliat',user_ID=2,email='akesode2015@gmail.com')
emp3 = Employee(name='John',user_ID=3,email='basket2014@gmail.com')
emp4 = Employee(name='Sarah',user_ID=4,email='johnson2012@gmail.com')
emp5 = Employee(name='Mike',user_ID=5,email='jones2011@gmail.com')
# %%
Group1 = Employee_group("Group_1")
Group2 = Employee_group("Group_2")

Group1.add_employee(emp1)
Group2.add_employee(emp2)
Group1.add_employee(emp3)
Group2.add_employee(emp4)
Group1.add_employee(emp5) 
# %%
list_all_employees()
list_all_groups()

EmailFunction.email_employee(emp2, f'Hello {emp2.name}, welcome to the team!')
EmailFunction.email_group(Group1, f'Hello {Group1.name}, this week is free coffee friday!')