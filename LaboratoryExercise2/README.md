# LaboratoryExercise2
 
# Preface to Checker/Reader

Laboratory Exercise 2

Author: Job Lipat

Date Created: May 17, 2020

Notes:

In this laboratory exercise, I continued the theme of using all the best practices that I know. I used a 3-tier architecture: the presentation layer where the UI functionalities are handled; the Business Logic layer where the data is queried; and the persistence layer where data is stored and retrieved. I designed the application so that each layer is encapulated as much as possible and knows little of each other and only interacts when needed. For example, the ViewModel doesn't know anything about how the Entity's data is serialized and it only knows that it should commit the model's state. I achieved this by making a class inherit FileBound and an Entity and the FileBound class is also abstract to allow entities to define how their data is could be used in serializing and deserializing. This allowed the program to do polymorphism and to treat the class as just another entity. The application also uses the factory pattern to allow dependency injection on the *strategy* of serializing and deserializing the values in the file. This means that the entity FileHandler is not responsible for *how* the data is going to be serialized or deserialized; instead, the factory injects the strategy to the entities. The application also uses a pseudo-MVC pattern as could be seen in the naming convention. I have also made a [testing plan](docs/Testing%20Plan.docx) (which is in the docs folder) to verify conformity to instructions.


## Responsibilities of Modules:

### Presentation Layer
| Module | Functionality |
| ------- | ------------- |
| [__ main __](__main__.py) | Entry Point of the program |
| [<*module*>ViewController](payroll/PayrollViewController.py) | Where the UI of the program is handled |


### Business Logic Layer
| Module | Functionality |
| -------| ------------- |
| [<*module*>ViewModel](payroll/PayrollViewModel.py) | The ViewModel is queried by the UI to get the necessary data. The ViewModel queries entities to get the necessary data. |
| [<*module*>EntityManager](payroll/PayrollEntityManager.py) | Collection of multiple types of entities/data objects. Structured Data |
| [<*module*>EntityManagerFactory](payroll/PayrollEntityManagerFactory.py) | Creates an EntityManager |
| [<*singular_entity_name*>Entity](payroll/entities/EmployeeEntity.py) | A singular data object |
| [<*plural_entity_name*>Entity](payroll/entities/EmployeesEntity.py) | A collection of a single type of entity/data object |
| [<*entity_name*>EntityView](payroll/entities/PayrollRecordEntityView.py) | A data object that is used to aid in presentation. Usually used to combine data from mutliple entities|


### Persistence Layer
| Module | Functionality |
| -------| ------------- |
| [FileBound](payroll/entities/filebound/FileBound.py) | Abstract class to provide file storage functionality |
| [FileBound<*entity_name*>Entity](payroll/entities/filebound/FileBoundEmployeesEntity.py) | A class that inherits FileBound and an Entity to provide file storage functionality for an entity |
| [FileDataHandler](data/FileDataHandler.py) | Encapsulates file reading and writing |

### Miscellaneous
| Module | Functionality |
| -------| ------------- |
| [CaseInsensitiveDict](lib/CaseInsensitiveDict.py) | A dictionary where the keys are case insensitive |
| [Helper](lib/Helper.py) | Helper functions to help UI |
| [StringRowValueEncoder](lib/StringRowValueEncoder.py) | Converts row-value array to a row-value string |
| [StringRowValueSplitter](lib/StringRowValueSplitter.py) | Converts row-value string to a row-value array |





## Instructions:

Write a program that will perform the following:

1. Display Employee List
 - Retrieve records from empList.txt)

2. Add Employee

- Ask user to input the following data:

    - unique employee number

    - lastname

    - firstname

    - department

    - rate per hour

- Write the employee record to the empList.txt

3. Add Payroll Record

- Ask user to input the following data:

    - employee number

    - month

    - no of days worked

- write the payroll record into the empMR.txt




4. Generate pay slip

- Ask for employee number and month of the payslip to be generated

- Create a payslip like statement written in a text file.

```
=================================================================

Payslip for the Month of _________________

Employee No.: ______________       Employee Name: _____________

Department: ________________

Rate per Day:_______________       No. of Days Worked: ________

Gross Pay: _________________

=================================================================   
```


## Validation

### Add Employee Record

- Employee Number (9-digits)

- last and Firstname (characters only)

- Department must one of the following: Accounting, Marketing, Human Resources, Finance, MIS, Admin

- Rate per Day (real numbers)



### Add Payroll Record

- Employee Number (must be of an existing employee)

- Month (1-12) only

- No. of Day : whole numbers (depend on the number of days of the given Month)

- There must be only one record for one employee for each month.



### Generate Payslip

- Employee No. (must of an existing employee)

- Month (1-12 and must be existing in the record)



# Rubric:

- Functionality      25

- Exception Handling   20

- File Manipulation  20

- Coding Style (Module/Functions,Data Structures) 20

- Formatting/Output Design 15

[Back to Project List](\..\README.md)
