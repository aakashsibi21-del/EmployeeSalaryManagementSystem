from Employee import Employee          # Importing Parent Class.

class Contract_Employee(Employee):        # Child Class. 
    def calculate_slary(self, Allowance):     # defining Abstract Method from parent class.
        Allowance = 0.05
        print( 'Total Salary  : ',self.Emp_salary + (self.Emp_salary * Allowance),'\n')