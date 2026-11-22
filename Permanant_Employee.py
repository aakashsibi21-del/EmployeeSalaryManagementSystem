from Employee import Employee         # Importing Parent class.

class Permenent_Employee(Employee):    # Child Class.
    def calculate_slary(self, Allowance):    # Defining Abstract method from parent class.
         Allowance = 0.2
         print( 'Total Salary  : ',self.Emp_salary + (self.Emp_salary * Allowance),'\n')