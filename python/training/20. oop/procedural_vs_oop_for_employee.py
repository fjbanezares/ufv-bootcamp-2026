# Procedural approach to managing employee data

# List to store employee data
employees = []

# Function to add a new employee
def add_employee(name, position, salary):
    employee = {'name': name, 'position': position, 'salary': salary}
    employees.append(employee)

# Function to update an employee's salary
def update_salary(name, new_salary):
    for employee in employees:
        if employee['name'] == name:
            employee['salary'] = new_salary
            return

# Function to calculate the total salary expense
def total_salary():
    total = 0
    for employee in employees:
        total += employee['salary']
    return total

# Using the functions
add_employee('Alice', 'Developer', 70000)
add_employee('Bob', 'Manager', 90000)
update_salary('Alice', 75000)

print(total_salary())  # Output: 165000

# Thank you for following! Now, let's look at the same example using OOP.


# Object-Oriented approach to managing employee data

# Defining the Employee class
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    # Method to update the salary
    def update_salary(self, new_salary):
        self.salary = new_salary

# Class to manage a collection of employees
class EmployeeManager:
    def __init__(self):
        self.employees = []

    # Method to add a new employee
    def add_employee(self, employee):
        self.employees.append(employee)

    # Method to calculate the total salary expense
    def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total

# Using the Employee and EmployeeManager classes
manager = EmployeeManager()

# Creating Employee objects
alice = Employee('Alice', 'Developer', 70000)
bob = Employee('Bob', 'Manager', 90000)

# Adding employees to the manager
manager.add_employee(alice)
manager.add_employee(bob)

# Updating salary using the Employee class method
alice.update_salary(75000)

print(manager.total_salary())  # Output: 165000

# Amazing! Thank you for your patience. Let's discuss why OOP might be better in this context.

'''Modularity and Reusability: OOP allows us to bundle data and methods together in a class, making code modular and reusable. In the employee management example, the Employee and EmployeeManager classes can be reused across different parts of the program or in other programs, unlike procedural functions that are more specific and less reusable.

Ease of Maintenance: As programs grow in complexity, OOP makes them easier to maintain and extend. Adding new features or modifying existing ones is often simpler because each class can be updated independently. For example, adding a new method to calculate bonuses would only require a change to the Employee class.

Encapsulation: OOP encapsulates data and behavior, reducing the risk of unintended interactions between different parts of the program. In the procedural approach, any function can modify the global employees list, leading to potential bugs. In the OOP approach, employee data is safely encapsulated within the Employee objects.'''


'''
When Procedural Programming Might Be Better:
Simplicity: For small, simple scripts or programs where you only need to perform a few straightforward tasks, procedural programming might be more straightforward and efficient. There is less overhead in writing and understanding the code.

Performance: In some cases, procedural programming can offer performance benefits because it involves fewer abstractions. Direct function calls and data manipulation can be faster than creating and managing objects, especially in computationally intensive tasks.

Learning Curve: For beginners, procedural programming can be easier to learn and understand. It introduces fundamental concepts of programming without the complexity of objects, inheritance, and polymorphism.
'''