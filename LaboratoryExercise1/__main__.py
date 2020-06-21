"""
## PREFACE TO CHECKER/READER:

Author: Job Lipat
Date Created: May 10, 2020


# Responsibilities of Modules and Recommended Checking Order:
__main__                                  -> The entry point of the program
empData                                   -> Contains the raw data
employees.EmployeesViewController         -> The user interface. Handles data input and output. Gets data from model
employees.EmployeesEntityManager          -> Contains structured data that contains relationships between entities
                                            -> Manager because contains multiple entities and relationships
                                            -> Entities are a keyed data structure where each item contains a key and multiple
                                               fields. Similar to database tables
employees.EmployeesEntityManagerBuilder   -> Creates an instance of EmployeesEntityManager Implements Builder Pattern
employees.EmployeesViewModel              -> Queries needed data from EmployeesEntityManager
                                             Data queried is used for EmployeesViewController
employees.StringRowValueSplitter          -> Helper class that is used in parsing empData
employees.Helper                          -> Helper functions


"""

from employees.EmployeesViewController import EmployeesViewController
from employees.EmployeesEntityBuilder  import EmployeesEntityManagerBuilder
from employees.EmployeesEntityManager  import EmployeesEntityManager
from employees.EmployeesViewModel      import EmployeesViewModel
from employees.StringRowValueSplitter  import StringRowValueSplitter
from employees.empData                 import empRecords

def main():
    splitter = StringRowValueSplitter(",",";")
    data = splitter.parse(empRecords)
    entityBuiler = EmployeesEntityManagerBuilder()
    entityManager = entityBuiler.setData(data).build()
    entityModel = EmployeesViewModel(entityManager)
    viewController = EmployeesViewController(entityModel)
    viewController.viewMenu()

main()

    
"""
INSTRUCTIONS:

Create program that will able the user to perform the following:
    A. Display No. of Employees
    B. List the Employee Name (Lastname, Firstname and age) of employees based on age range (bottom, top).
    C. List of Employees (Lastname, Firstname and City) residing in a given city
    D. Display number of employee in a given county.
    E. Count no. of employee by email provider site.

Note:
    Employee Record is composed of the following:
        first_name
        last_name
        address
        city
        county
        state
        bdate
        zip
        phone1
        phone2
        email
        web
        
    In the given string from the module empData, Each employee data is separated by comma (,). Each record is separated by semicolon (;).

Rubric:
    Functionality 40
    Appropriate use of data structure (list, tuples, dict, sets) 20
    Able to use String and Date function 10
    Create appropriate user-defined function/modules to accomplish the tasks. 20
    Program Design/Output consideration. 10
"""
