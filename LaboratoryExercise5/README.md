# LaboratoryExercise2
 
# Preface to Checker/Reader

Laboratory Exercise 5

Author: Job Lipat

Date Created: June 21, 2020

Notes:

I'm sorry that I have given up documenting my code. I realized that documenting code takes too much time and I have to do something about it. In the future, I will try to create/use a auto documentor that compiles the docuemntation of all modules. That way I just have to update the documentation on the code and not the document itself. 

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
| [FileEncoder](payroll/filestrategy/FileEncoder.py) | Converts row-value array to a row-value string |
| [FileParser](payroll/filestrategy/FileParser.py) | Converts row-value string to a row-value array |





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
