from Permanant_Employee import Permenent_Employee
from Contract_Employee import Contract_Employee

Per = Permenent_Employee('BatMan', 2056, 'Teaching Staf', 'Physics', 80000)
Con = Contract_Employee('Thor', 4068, 'Non Teaching Staf', 'Chemistry', 60000)

Per.Display_Details()
Per.calculate_slary(0.2)

Con.Display_Details()
Con.calculate_slary(0.05)