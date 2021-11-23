def email_group(group, msg):
    for employee in group.list_of_employees:
        print(f'Emailing {employee.email},{msg}')

def email_employee(employee, msg):
    print(f'Emailing {employee.email},{msg}')