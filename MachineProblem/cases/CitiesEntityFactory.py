from payroll.entities.filebound.FileBoundEmployeesEntity import FileBoundEmployeesEntity
from payroll.entities.filebound.FileBoundPayrollsEntity import FileBoundPayrollsEntity
from payroll.PayrollEntityManager import PayrollEntityManager
from lib.StringRowValueEncoder import StringRowValueEncoder
from lib.StringRowValueSplitter import StringRowValueSplitter
from data.FileDataHandler import FileDataHander
import os

class PayrollEntityManagerFactory:
    """ Factory class for PayrollEntityManager. Creates FileBoundEntities instead of normal entities """
    
    def create(self):
        cwd = os.getcwd()
        encoder = StringRowValueEncoder(",","\n")
        splitter = StringRowValueSplitter(",","\n")
        fileHandler = FileDataHander(cwd + "\\data\\empList.txt")
        factory = FileBoundCityFactory()
        cities = FileBoundCities(fileHandler, splitter, encoder, factory)
        cities.retrieveState()
        
        return PayrollEntityManager(cities)
        