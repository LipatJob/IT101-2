class EmployeesEntityManager:
    def __init__(self, builder):
        self.cities         = builder.cities
        self.counties       = builder.counties
        self.states         = builder.states
        self.emailProviders = builder.emailProviders
        self.employees      = builder.employees