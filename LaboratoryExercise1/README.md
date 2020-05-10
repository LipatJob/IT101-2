# LaboratoryExercise1

## Preface to Reader/Checker

Author: Job Lipat

Date Created: May 10, 2020


### Responsibilities of Modules:

#### __ main __
* The entry point of the program

#### empData
* Contains the raw data

#### employees.EmployeesViewController
* The user interface. Handles data input and output. Gets data from model

#### employees.EmployeesEntityManager
* Contains structured data that contains relationships between entities. The class is a manager because contains multiple entities and relationships. Entities are a keyed data structure where each item contains a key and multiple fields. Similar to database tables

#### employees.EmployeesEntityManagerBuilder
* Creates an instance of EmployeesEntityManager Implements Builder Pattern

#### employees.EmployeesViewModel
* Queries needed data from EmployeesEntityManager. Data queried is used for EmployeesViewController

#### employees.StringRowValueSplitter
* Helper class that is used in parsing empData

#### employees.Helper
* Helper functions

## Instructions:

Create program that will able the user to perform the following:


1. Display No. of Employees

2. List the Employee Name (Lastname, Firstname and age) of employees based on age range (bottom, top).

3. List of Employees (Lastname, Firstname and City) residing in a given city

4. Display number of employee in a given county.

5. Count no. of employee by email provider site.

Note:

Employee Record is composed of the following:


* first_name
* last_name
* address
* city
* county
* state
* bdate
* zip
* phone1
* phone2
* email
* web
        
In the given string from the module empData, Each employee data is separated by comma (,). Each record is separated by semicolon (;).

Rubric:
* Functionality: 40
* Appropriate use of data structure (list, tuples, dict, sets): 20
* Able to use String and Date function: 10
* Create appropriate user-defined function/modules to accomplish the tasks: 20
* Program Design/Output consideration: 10

[Back to Project List](\..\README.md)
