""" Please open README.md using a markdown editor to see the functionalities of the modules """


from cases.CitiesViewModel import CitiesViewModel
from cases.CitiesEntityFactory import CitiesEntityFactory
from cases.filebound.FileBoundCityFactory import FileBoundCityEntityFactory
from cases.CitiesViewController import CitiesViewController


def main():
    entityFactory = CitiesEntityFactory()
    entity = entityFactory.create()
    cityFactory = FileBoundCityEntityFactory()
    viewModel = CitiesViewModel(entity, cityFactory)
    viewController = CitiesViewController(viewModel)
    viewController.viewMenu()
main()
