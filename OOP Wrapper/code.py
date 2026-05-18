
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")

class Employee(Person):
    def __init__(self,name,age,employee_id,salary):
        super().__init__(name,age)
        self.__employee_id=employee_id
        self.__salary=salary

    def get_id(self):
        return self.__employee_id
        
    def set_id(self,eid):
        self.__employee_id=eid    
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,salary):
        if salary > 0:
            self.__salary = salary

    def display(self):
        super().display()
        print(f"Employee ID : {self.__employee_id}")
        print(f"salary {self.__salary}")

    def __del__(Self):
        pass    


class Manager(Employee):

    def __init__(self,name,age,employee_id,salary,department):
        super().__init__(name,age,employee_id,salary)
        self.department=department

    def display(self):
        super().display()
        print(f"Department : {self.department}")


class Developer(Employee):
    def __init__(self,name,age,employee_id,salary,language):
        super().__init__(name,age,employee_id,salary)
        self.language=language

    def display(self):
        super().display()
        print(f"Programming Language : {self.language}")    
               


def main_menu():
    employees=[]


    while True:
        print("\n Python OOP Project: Employee Management System")
        print("\nChoose a an operation : \n")
        print("1.Create a person")
        print("2.Create an Employee")
        print("3.Create a Manager")
        print("4.Show Details")
        print("5.Exit")

        select=input("Enter your choice : ")

        if select=="1":
            name=input("name : ")
            age=int(input("Age : "))
            employees.append(Person(name,age))
            print(f"Person created  :{name} age : {age}")   

        elif select=="2":
            name=input("Enter name : ")
            age=int(input("Enter Age : "))
            eid=input("Enter Employee ID : ")
            sal=int(input("Enter salary : "))
            employees.append(Employee(name,age,eid,sal))
            print(f"employee created With Name : {name},age : {age},ID : {eid} and salary : {sal}")

        elif select=="3" or select=="03":
            name=input("Enter Name : ")
            age=int(input("Enter Age : "))
            eid= input("Enter Employee ID: ")
            sal = int(input("Enter Salary: "))
            dept = input("Enter Department: ")
            employees.append(Manager(name,age,eid,sal,dept))
            print(f"Manager created with name : {name},age : {age},ID : {eid}, salary : {sal} and Department : {dept}")


        elif select=="4" or select=="04":
            if not employees:
                print("No Data Found ! ")
                continue

            print("\n Choose Details show : ")
            print(f"1.person")
            print(f"2.Employee")
            print(f"3.Manager")
            sub_choice= input("Enter your choice : ")

            if sub_choice =="1":
                t_class=Person
            elif sub_choice=="2":
                t_class=Employee
            else:
                t_class = Manager       

            print("\n Details")
            for emp in employees:
                if type(emp) == t_class:
                    emp.display()



        elif select=="5" or select=="05":
            print("Exiting the system. All resources have been freed.")
            print("Goodbye!")
            break

if __name__=="__main__":
    main_menu()
    
