""" Please open README.md using a markdown editor to see the functionalities of the modules """

from payroll.PayrollEntityManagerFactory import PayrollEntityManagerFactory
from payroll.PayrollViewController import EmployeesViewController
from payroll.PayrollViewModel import PayrollViewModel

def main():
    factory = PayrollEntityManagerFactory()
    manager = factory.create()
    viewModel = PayrollViewModel(manager)
    viewController = PayrollViewController(viewModel)
    viewController.viewMenu()

main()
