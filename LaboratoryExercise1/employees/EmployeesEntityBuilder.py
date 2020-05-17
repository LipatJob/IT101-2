from datetime import datetime
from lib.CaseInsensitiveDict import CaseInsensitiveDict
from employees.EmployeesEntityManager import EmployeesEntityManager

class EmployeesEntityManagerBuilder:
    """ Creates an instance of an EmployeesEntityManager
    
    Attributes
    ----------
    cities : CaseInsensitiveDict
        list of cities of the employees
    counties : CaseInsensitiveDict
        list of countries of the employees
    states : CaseInsensitiveDict
        list of states of the employees
    emailProviders : CaseInsensitiveDict
        list of email providers of the employees
    employees : dict
        the emplyees
    _employeeMetadata : tuple
        Meta data of a single Employee Entity
        
    Notes
    -----
    Implements the builder design pattern but individual entities does not implement it because entities are implemented as dicts. 
    dict() is used to allow non integer indices and to allow O(1) lookup for non integer indices.
        also does not corrupt data on value deletion
    Builder Pattern: https://sourcemaking.com/design_patterns/builder
        
    """
    def __init__(self):
        self.cities         = CaseInsensitiveDict() 
        self.counties       = CaseInsensitiveDict()
        self.states         = CaseInsensitiveDict()
        self.emailProviders = CaseInsensitiveDict()
        self.employees      = dict()
        self._employeeMetadata = (
                ("first_name", str),
                ("last_name" , str),
                ("address", str),
                ("city", str),
                ("county", str),
                ("state", str),
                ("bdate", self._dateTypeWrapper),
                ("zip", str),
                ("phone1", str),
                ("phone2", str),
                ("email", str),
                ("web", str),
        )
        
        
    def setData(self, data):
        """ Binds data to attributes and creates relationships
        
        The method also creates relationships:
            employee['city'] +--< city                [crowfoot notation]
            employee['county'] +--< county
            employee['state'] +--< state
            employee['email'] +--< emailProviders
        
        Data structure of `data` parameter:
            [
                [
                    first_name,  last_name,  address,  city,  county,  state,  bdate,  zip,  phone1,  phone2,  email,  web
                ], ... < similar to previous item > ...
            ]
        
        args
        ----
            data : list of employee detail values
        
        return
        ------
            self : returns itself to allow method chaining
        
        """
        for row in data:
            employeeData = dict()

            # Bind metadata and data
            for (key, dataType), entry in zip(self._employeeMetadata, row):
                employeeData[key] = dataType(entry)

            # Create key and bind key to data
            key = self._getMaxIndex(self.employees)
            self.employees[key] = employeeData
            
            # Setup Relationships
            self._createRelationship(self.cities, employeeData["city"], key)
            self._createRelationship(self.counties, employeeData["county"], key)
            self._createRelationship(self.states, employeeData["state"] ,key)
            emailProvider = employeeData["email"].split("@")[1]
            self._createRelationship(self.emailProviders, emailProvider, key)
        
        # Allow Method Chaining
        return self

        
    def build(self):
        """ Creates an instace of the object using the builder """
        entityManager = EmployeesEntityManager(self)
        return entityManager


    def _createRelationship(self, dictRel, key, value):
        """ Allows related data to be easily accessible. Related data can be referenced though a dictionary key """
        if key not in dictRel:
            dictRel[key] = list()
        dictRel[key].append(value)


    def _dateTypeWrapper(self, date):
        """Creates a datetime object from a string with the format 'MM/DD/YYYY' """
        month, day, year = [int(x) for x in date.split("/")]
        return datetime(year, month, day)


    def _getMaxIndex(self, values):
        """ Returns the max index of a list. Max index is used to create a key """
        return len(values.keys())    
    

        