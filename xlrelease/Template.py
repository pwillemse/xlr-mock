class Template(object):

    def __init__(self, title):
        self.title = title
        self.phases = []
        self.variables = []

    def add_phase(self, phase):
        self.phases.append(phase)

    def add_variable(self, variable):
        self.variables.append(variable)

    def get_phases(self):
        return self.phases

    def get_title(self):
        return self.title

    def get_variables(self):
        return self.variables
