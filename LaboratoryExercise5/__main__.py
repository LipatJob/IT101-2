""" Please open README.md using a markdown editor to see the functionalities of the modules """

from src.entities.EntityManager import *
from src.ViewController import ViewController
from src.ViewModel import ViewModel

def main():
    factory = EntityManagerFactory()
    manager = factory.create()
    manager.retrieveState()
    viewModel = ViewModel(manager)
    viewController = ViewController(viewModel)
    viewController.viewMenu()
    
main()
    
    

