class Employee:

    employee_class = 'Employee'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.employee_class}'s name is {self.name} and his salary is {self.salary} c.u."

class Manager(Employee):

    employee_class = 'Manager'

    def __init__(self, name, salary, department):
        Employee.__init__(self,name, salary)
        self.department = department

class Developer(Employee):

    employee_class = 'Developer'

    def __init__(self, name, salary, programming_language):
        Employee.__init__( self,name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):

    employee_class = 'TeamLead'

    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


# team_lead = TeamLead('Eric', 100, department="DevOps", programming_language='Python', team_size=3)
# print(team_lead)
#
# employee = Employee('Nick', 80)
# print(employee)
