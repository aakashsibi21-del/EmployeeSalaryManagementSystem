from Employee import Employee

class Contract_Employee(Employee):
    def calculate_slary(self, Allowance):
        Allowance = 0.05
        print( 'Total Salary  : ',self.Emp_salary + (self.Emp_salary * Allowance),'\n')