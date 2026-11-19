from Employee import Employee

class Permenent_Employee(Employee):
    def calculate_slary(self, Allowance):
         Allowance = 0.2
         print( 'Total Salary  : ',self.Emp_salary + (self.Emp_salary * Allowance),'\n')