""" Please open README.md using a markdown editor to see the functionalities of the modules """
# Text files are stored in the data folder

from payroll.PayrollEntityManagerFactory import PayrollEntityManagerFactory
from payroll.PayrollViewController import PayrollViewController
from payroll.PayrollViewModel import PayrollViewModel

def main():
    factory = PayrollEntityManagerFactory()
    manager = factory.create()
    viewModel = PayrollViewModel(manager)
    viewController = PayrollViewController(viewModel)
    viewController.viewMenu()

main()

