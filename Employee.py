from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, Emp_Name, Emp_id, Emp_role, Emp_Department, Emp_salary):
        self.Emp_name = Emp_Name
        self.Emp_id = Emp_id
        self.Emp_role = Emp_role
        self.Emp_Department = Emp_Department
        self.__Emp_salary = Emp_salary

    @abstractmethod
    def calculate_slary(self):
        pass

    @property
    def Emp_salary(self):
        return self.__Emp_salary

    def Display_Details(self):
        print('\nEmployee Name : ',self.Emp_name,'\nEmployee Id   : ',self.Emp_id,
              '\nEmployee Role : ',self.Emp_role)